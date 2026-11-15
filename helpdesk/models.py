"""The database tables, one class per table, as drawn in the ERD.

Each class attribute is a column. Mapped[...] says what type of Python value
the column holds; "| None" means the column may be empty (NULL).
"""
from datetime import datetime, timedelta

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from .extensions import db

# The allowed values for each choice field. Forms and checks use these
# lists, so a field can never hold a value that is not on its list.
ROLES = ["customer", "tier1", "tier2", "tier3", "manager"]
STAFF_ROLES = ["tier1", "tier2", "tier3", "manager"]
ENGINEER_ROLES = ["tier2", "tier3"]
CATEGORIES = ["hardware", "software", "network", "account", "other"]
PRIORITIES = ["low", "medium", "high", "critical"]
STATUSES = ["new", "open", "waiting", "resolved", "closed"]
TIERS = [1, 2, 3]
JOB_KINDS = ["installation", "maintenance", "repair"]
JOB_STATUSES = ["scheduled", "in_progress", "done", "cancelled"]
TEXT_SIZES = ["normal", "large", "larger"]

# How each role is written on the pages.
ROLE_LABELS = {
    "customer": "Customer",
    "tier1": "Tier 1",
    "tier2": "Tier 2",
    "tier3": "Tier 3",
    "manager": "Manager",
}


class Company(db.Model):
    """A small business that Netheret supports."""
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    address: Mapped[str] = mapped_column(String(250))
    phone: Mapped[str] = mapped_column(String(30))


class User(db.Model):
    """Anybody who signs in: a customer or a member of Netheret's staff."""
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    # Only a one-way hash of the password is kept, never the password itself.
    password_hash: Mapped[str] = mapped_column(String(256))
    role: Mapped[str] = mapped_column(String(20))
    # Only customers belong to a company, so staff leave this empty.
    company_id: Mapped[int | None] = mapped_column(ForeignKey("company.id"))
    # Accessibility settings, saved per user.
    text_size: Mapped[str] = mapped_column(String(10), default="normal")
    high_contrast: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    company: Mapped["Company"] = relationship()

    def set_password(self, password):
        # generate_password_hash adds a random salt, so two users with the
        # same password still get different hashes.
        hashed = generate_password_hash(password)
        self.password_hash = hashed

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_staff(self):
        return self.role in STAFF_ROLES


class Ticket(db.Model):
    """A support request."""
    id: Mapped[int] = mapped_column(primary_key=True)
    # The reference customers quote, like NTH-0001. It is made from the id,
    # so it is filled in just after the ticket is first saved.
    reference: Mapped[str | None] = mapped_column(String(12), unique=True)
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(20))
    priority: Mapped[str] = mapped_column(String(10))
    status: Mapped[str] = mapped_column(String(10), default="new")
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    raised_by_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    assigned_to_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))
    tier: Mapped[int] = mapped_column(default=1)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    resolved_at: Mapped[datetime | None]

    company: Mapped["Company"] = relationship()
    # Two columns point at the user table, so each relationship says which.
    raised_by: Mapped["User"] = relationship(foreign_keys=[raised_by_id])
    assigned_to: Mapped["User"] = relationship(foreign_keys=[assigned_to_id])
    updates: Mapped[list["TicketUpdate"]] = relationship(
        back_populates="ticket", order_by="TicketUpdate.created_at"
    )

    def set_reference(self):
        self.reference = f"NTH-{self.id:04d}"


class TicketUpdate(db.Model):
    """One entry on a ticket's timeline: a note, a reply or a status change."""
    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("ticket.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    body: Mapped[str] = mapped_column(Text)
    # False means an internal note that only staff can read.
    visible_to_customer: Mapped[bool] = mapped_column(default=False)
    # The new status, when this update changed it, for example "resolved".
    status_change: Mapped[str | None] = mapped_column(String(10))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    ticket: Mapped["Ticket"] = relationship(back_populates="updates")
    author: Mapped["User"] = relationship()


class Job(db.Model):
    """On-site work by an engineer at a customer's premises."""
    id: Mapped[int] = mapped_column(primary_key=True)
    # A job may come from a ticket, or be planned work with no ticket.
    ticket_id: Mapped[int | None] = mapped_column(ForeignKey("ticket.id"))
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    engineer_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    title: Mapped[str] = mapped_column(String(150))
    brief: Mapped[str] = mapped_column(Text)
    kind: Mapped[str] = mapped_column(String(20))
    scheduled_start: Mapped[datetime]
    duration_minutes: Mapped[int]
    status: Mapped[str] = mapped_column(String(20), default="scheduled")
    notes: Mapped[str] = mapped_column(Text, default="")

    ticket: Mapped["Ticket"] = relationship()
    company: Mapped["Company"] = relationship()
    engineer: Mapped["User"] = relationship()

    @property
    def scheduled_end(self):
        return self.scheduled_start + timedelta(minutes=self.duration_minutes)

    def can_be_seen_by(self, user):
        """Managers and Tier 1 see every job; an engineer sees their own."""
        return user.role in ["manager", "tier1"] or self.engineer_id == user.id

    def can_be_updated_by(self, user):
        return user.role == "manager" or self.engineer_id == user.id


class Article(db.Model):
    """A knowledge base article: a known problem and how to fix it."""
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    symptoms: Mapped[str] = mapped_column(Text)
    solution: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(20))
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    views: Mapped[int] = mapped_column(default=0)
    helpful_count: Mapped[int] = mapped_column(default=0)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

    author: Mapped["User"] = relationship()
