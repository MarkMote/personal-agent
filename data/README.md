# Data

## Source Lists (Research Pool)

Companies segmented by stage, not yet in active outreach:

| File | Stage |
|------|-------|
| `early.csv` | Seed / Series A startups |
| `mid.csv` | Series B-D companies |
| `late.csv` | Big tech / late-stage (DeepMind, Meta FAIR, etc.) |
| `out.csv` | Outside NYC (SpaceX, Relativity, etc.) |

**Schema:** Company, Description, Location, Comp Range, Tier, Notes

## Active Funnel

`tracker.csv` - Companies moved into active outreach pipeline.

**Schema:** Priority, Company, Category, Day, Contact, Resume, Status, Date Applied, Response, Next Step, Notes

Companies get promoted from source lists → tracker.csv when ready to pursue.
