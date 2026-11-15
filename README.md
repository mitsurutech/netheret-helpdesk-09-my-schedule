# Netheret help desk, step 09: my schedule

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step gives Tier 2 and Tier 3 engineers their own schedule and a job brief
for each job, where they mark their progress.

## What this step adds

In `helpdesk/jobs.py`:

- `/jobs/mine`: an engineer's jobs from today onwards, grouped by day, plus
  any older job still marked "in progress".
- `/jobs/<id>`: the job brief: when, where, the customer's phone number, the
  brief, and the customer's original problem if the job came from a request.
- `/jobs/<id>/progress`: the engineer moves the job to "in progress" or
  "done" and writes notes. When a job from a request is done, a note goes on
  that request's timeline.

In `helpdesk/models.py`, `Job.can_be_seen_by()` and `Job.can_be_updated_by()`
keep the rules about who may see and change a job in one place. The week
view and the brief page both use them.

## Run it

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Sign in as `tier2@netheret.example` or `tier3@netheret.example` (demo
password `password123`) and open My schedule. Try to open another
engineer's job from the week view: there is no link, and typing the address
gives 403.

## What to look at

- `days.setdefault(day, []).append(job)`: a short way to group a list into a
  dictionary of lists.
- An engineer cannot cancel a job. The form leaves that choice out, and the
  server refuses it too, because a form can be changed by the person using it.
- `finished_now`: the timeline note is only written the first time a job
  becomes done, not every time the notes are saved.

<!-- links -->
