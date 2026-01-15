# Outbound Research & Outreach Prep

Prepare outreach for a company. Creates strategy, messages, and adds to queue.

## Arguments
- $ARGUMENTS: Company name (e.g., "viam" or "icarus robotics")

## Workflow

1. **Find the company folder** in `company-intel/00_pending/` (match by name)

2. **Read `full_context.md`** - Mark will have added raw research (JDs, news, LinkedIn notes, contacts, warm paths)

3. **Synthesize and ask questions** if anything is unclear:
   - Who is the target contact?
   - What's the warm path situation?
   - Any role preference or constraints?

4. **Update files:**

   a. **`{company}.md`** - Synthesized research:
      - Quick facts (location, stage, funding, team size)
      - Problem they're solving
      - Their approach/tech stack
      - Key people table
      - Open roles with comp and fit assessment
      - Your angle (resume variant, why you, hook)
      - Warm paths
      - Application notes

   b. **`outreach.md`** - Execution plan:
      - Strategy summary (tier, approach, target role, resume variant)
      - Contacts table with status
      - Execution sequence (what happens when)
      - Messages: initial + 2 follow-ups
      - Post-response instructions (including tier-specific delay rules)

   c. **`data/outreach_queue.csv`** - Add rows:
      - Initial message (Status: Queued, Scheduled: send date)
      - Follow-up 1 (Status: Pending, Scheduled: +5 days)
      - Follow-up 2 (Status: Pending, Scheduled: +12 days)

   d. **`data/tracker.csv`** - Update contact name if found

5. **Move company folder** from `00_pending/` to `02_qualified/`

6. **Confirm with Mark** - Show the initial message for review before finalizing

## Message Format

```
[1 sentence] Who you are + credibility anchor
[2-3 sentences] Why them specifically / what you understand about their problem
[1 sentence] What you're looking for + clear ask
```

- LinkedIn DM: 3-5 sentences (~100-150 words)
- Reference specific things about the company (mission, recent news, tech challenges)
- Paul Graham style: simple, real, professional but not overly formal

## Tier-Specific Scheduling Notes

| Tier | Technical Screen Approach |
|------|---------------------------|
| 0 (startup) | Aim 7-14 day delay, but take shot if they won't wait |
| 0 (big co) | Delay until W07+ calibration complete |
| 1 | Delay once by 7-14 days |
| 2 | Schedule normally - use for calibration |
