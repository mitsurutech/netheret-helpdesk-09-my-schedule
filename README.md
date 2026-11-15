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

## Learn this step

This is step 9 of 16 of **Task 2. Developing the solution**, a free series of T Level Digital Software Development
lessons that builds the Netheret help desk in agile sprints with Python and Flask. Read the lesson for this step:
[An engineer's schedule and job briefs](https://mitsurutech.co.uk/resources/t-level/dsd-t2-09-my-schedule).

- Previous step: [step 08, scheduling on-site jobs](https://github.com/mitsurutech/netheret-helpdesk-08-jobs)
- Next step: [step 10, the knowledge base](https://github.com/mitsurutech/netheret-helpdesk-10-knowledge-base)
- [Every free T Level Digital lesson](https://mitsurutech.co.uk/resources/t-level)
- [Teach these lessons to your class on MitsuruTech](https://mitsurutech.co.uk/learning), [see the pricing](https://mitsurutech.co.uk/pricing) or
  [start a free year for your college](https://mitsurutech.co.uk/signup)

## About

Written by [Mitsuru Technologies](https://mitsurutech.co.uk) (MitsuruTech) as a teaching example for T Level Digital
Software Development. The Netheret IT Support Solutions brief is from Pearson's sample assessment material; this code
and its notes are our own, and are not published, endorsed or approved by Pearson or the Department for Education.
'T Level' is a registered trade mark of the Department for Education.

