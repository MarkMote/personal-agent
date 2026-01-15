# Wave 1 Outreach Action Plan

## Overview
- **48 companies** in `tracker.csv`
- **Goal:** By end of week, have all initial messages ready and start sending
- **Target:** Responses → conversations → opportunities by March-April

---

## Interview Staging Strategy

**Core insight:** You control when you enter evaluation mode, not when you start conversations.

- **Start intros immediately** — no downside to early conversations
- **Stage technical interviews intentionally** — don't burn top targets while rusty

### The Three Buckets

| Bucket | Timing | Who | Purpose |
|--------|--------|-----|---------|
| 🟢 Intros/Discovery | Now | Everyone | Build relationships, learn scope, enter pipelines |
| 🟡 Calibration Interviews | W06-W07 | Tier 2 | Shake off rust, identify weaknesses, practice |
| 🔴 Peak Interviews | W08+ | Tier 0 & 1 | Perform at peak readiness |

### Tier Definitions

**Tier 0 — All-stars (10 companies). Maximum protection.**
Icarus, Viam, Meta FAIR, DeepMind, DESRES, Jane Street, Osmo, OpenAI, Anthropic, Nanotronics

Technical interviews only after calibration complete (~W07+). These are career-defining opportunities.

**Tier 1 — Protect (9 companies). Delay technical screens 7-14 days.**
Standard Bots, MS Research, Anduril, Applied Intuition, Two Sigma, Citadel, HRT, K2 Space, Vannevar Labs

Strong targets where you want to perform well but can use flexibility.

**Tier 2 — Calibration (41 companies). Schedule normally.**
Everyone else NYC-compatible. Use for practice, rust removal, and pipeline building.

**Tier 3 — Last resort (9 companies). Only if NYC underperforms.**
Honeybee, Aetherflux, NVIDIA, Skild, Physical Intelligence, SpaceX, Blue Origin, etc.

Requires relocation. Don't spend W03-W05 energy here.

### Scheduling Rules

1. Accept every intro/recruiter call immediately
2. When asked to schedule a technical screen:
   - **Tier 2** → schedule normally (starting Feb 1)
   - **Tier 1** → ask for 7-14 days delay (once)
   - **Tier 0** → delay until calibration complete (~W07+)
3. Never delay the same company twice
4. Target 3-4 calibration interviews (Tier 2) before hitting Tier 0/1 technical loops

### Delay Script

When a Tier 1 company wants to schedule technical:

> "Sounds great. I'm wrapping up some prior commitments. Can we schedule for [date 7-14 days out]?"

This is normal and expected. Don't overthink it.

### Flexibility Rules (The Plan is a Default, Not a Law)

**Caveat 1:** Some Tier 1 companies won't tolerate deferral. If they say "this week or never," take the shot. Don't lose a top opportunity over scheduling purity.

**Caveat 2:** Tier 2 may move slower than expected. If Tier 2 under-delivers on calibration reps, use a fast-moving Tier 1 for practice if needed.

**Caveat 3:** 5-10 active Tier 1 processes is optimistic for NYC robotics. Realistic: 2-4 Tier 1, 3-5 Tier 2. Lower volume ≠ failure.

### Operational Rules

**Rule 1 — Always accept intro calls immediately.**
No gating. No delaying. No filtering except obvious spam.

**Rule 2 — Technical scheduling policy.**
- Tier 2: Schedule normally starting Feb 1
- Tier 1: Delay once by 7-14 days if possible; if pushed hard, accept earlier
- Tier 0: Delay until calibration complete (~W07+); if forced earlier, treat as Tier 1
- Never delay the same company twice

**Rule 3 — Pipeline load cap.**
- Max 3 active technical pipelines concurrently
- Max 2 interviews per day
- If exceeded, delay lower-priority companies

This protects prep quality.

**Rule 4 — Weekly checkpoint (every Friday).**
Review:
- Number of active pipelines
- How many technicals scheduled next week
- Weeks of runway remaining

Adjust aggressiveness accordingly. Prevents silent drift.

---

## Phase 1: Research & Contact Finding

### What to do for each company

**Step 1.1: Find the right contact(s)**

| Company Type | Target Contact | Backup |
|--------------|----------------|--------|
| Early startup (<50 ppl) | CEO or CTO | Lead Engineer |
| Growth startup | VP Eng / Eng Manager | Senior IC |
| Large company / Lab | Eng Manager or Senior IC | Another team member |

**Where to look:**
- Company website → Team page
- LinkedIn → Company page → People
- Recent news/press releases (often quote key people)
- Job postings (sometimes list hiring manager)

**What to capture per contact:**
- Name
- Role
- LinkedIn URL
- Email (if findable)
- Warm path? (mutual connections, GT alumni, shared background)

**Step 1.2: Understand their bleeding neck**

Look for:
- What roles are they hiring for right now? (careers page, LinkedIn jobs)
- Recent funding? (signals growth, urgency to hire)
- Recent product launches or technical announcements?
- What does the CEO/CTO post about on LinkedIn? (reveals priorities)

**Step 1.3: Identify your hook**

Answer: Why would this specific person reply to you?
- Technical overlap (spacecraft controls, CV, robotics, optimization)
- Founder-to-founder connection
- Specific knowledge of their problem domain
- Shared background (GT, JPL, etc.)

### Where things go

```
company-intel/00_pending/{company}/
├── {company}.md       ← Update: Key People table, Your Angle section
├── full_context.md    ← Dump: raw research, JD text, LinkedIn snippets, news
└── outreach.md        ← Create: contacts table, messages (Phase 2)
```

### Division of labor

| Task | Who |
|------|-----|
| LinkedIn/website research | Mark (requires login, browsing) |
| Checking GT alumni network | Mark |
| Synthesizing research into hooks | Claude (give me the raw info, I'll help frame it) |
| Drafting the contact table | Claude (give me names/roles, I'll format) |
| Identifying warm paths | Mark (only you can see mutual connections) |

---

## Phase 2: Message Drafting

### Message structure (all messages)

```
[1 sentence] Who you are + credibility anchor
[2-3 sentences] Why them specifically / what you understand about their problem
[1 sentence] What you're looking for + clear ask
```

**Length targets:**
- LinkedIn DM: 3-5 sentences (~100-150 words)
- Email: ~150 words
- LinkedIn connection note: <300 characters

### What to draft per contact

1. **Initial message** (LinkedIn or Email)
2. **Follow-up 1** (+5 days, short bump)
3. **Follow-up 2** (+12 days, graceful close)

### Follow-up templates

**Follow-up 1 (Day +5):**
> Floating this back up—I know [relevant context: fundraising, product launch, etc.] keeps things busy. Still interested in connecting if you have 15 minutes.

**Follow-up 2 (Day +12):**
> Going to assume you're heads down. I'll keep following [Company]'s work on [specific thing]. If timing is ever better, happy to reconnect.

### Where things go

Create `outreach.md` in each company folder:

```markdown
# Outreach: {Company}

## Contacts

| Name | Role | Channel | Warm Path | Status | Sent | Next Action |
|------|------|---------|-----------|--------|------|-------------|
| | | | | Queued | | |

## Messages

### {Contact Name}

**Initial ({Channel}):**
> Message here

**Follow-up 1 (Day +5):**
> Message here

**Follow-up 2 (Day +12):**
> Message here
```

### Division of labor

| Task | Who |
|------|-----|
| Writing first draft of messages | Claude (give me: contact name, company, your hook, any specific details) |
| Reviewing/editing messages | Mark (tone, accuracy, personal touch) |
| Writing follow-ups | Claude (I'll draft based on initial message) |
| Finalizing all messages | Mark (final approval before send) |

---

## Phase 3: Sending

### Execution sequence

Don't over-systematize. Work through the list at a sustainable pace.

**Suggested approach:**
- Start with highest-priority companies (Tier 1)
- Send 5-10 per day max (leaves bandwidth to respond)
- Morning sends (Tue-Thu) tend to get better response rates
- Avoid Monday morning (inbox flood) and Friday afternoon (checked out)

### Per-send checklist

Before hitting send:
- [ ] Correct name and company (no copy-paste errors)
- [ ] Something specific about them/their company
- [ ] Clear ask (15-min call)
- [ ] LinkedIn profile polished (they will look)

### After sending

Update immediately:
1. `outreach.md` → Status = "Sent", add date
2. `tracker.csv` → Update status column

### Division of labor

| Task | Who |
|------|-----|
| Actually sending messages | Mark (requires your accounts) |
| Updating status in files | Mark (or tell me what to update) |
| Reminding you of follow-up timing | Claude (if you want, share current status) |

---

## Phase 4: Follow-up & Response Management

### Follow-up cadence

| Touch | Timing | Action |
|-------|--------|--------|
| Initial | Day 0 | Send first message |
| Follow-up 1 | Day +5 | Short bump |
| Follow-up 2 | Day +12 | Graceful close |
| Archive | Day +14 | Stop. Mark as "No Response" |

### When they respond

**Positive response:**
- Reply within 4-6 hours
- Suggest 2-3 specific times
- Confirm day before call

**Neutral/curious response:**
- Answer their question directly
- Re-state the ask

**Negative response:**
- Thank them graciously
- Ask if there's someone else you should talk to
- Mark as closed, move on

### Status values for tracking

Use these in `outreach.md` and `tracker.csv`:

| Status | Meaning |
|--------|---------|
| `Queued` | Ready to send |
| `Sent` | Initial message sent |
| `Follow-up 1` | First follow-up sent |
| `Follow-up 2` | Second follow-up sent |
| `Responded` | They replied (any response) |
| `Scheduled` | Call/meeting scheduled |
| `Interviewing` | Active interview process |
| `Dead` | No response after all touches, or explicit rejection |

### Division of labor

| Task | Who |
|------|-----|
| Sending follow-ups | Mark |
| Drafting responses to their replies | Claude (share what they said, I'll help draft) |
| Prepping for scheduled calls | Claude (I'll pull together company context) |
| Updating status | Mark |

---

## Daily/Weekly Workflow

### Daily (during active outreach)
1. Check for responses → reply quickly
2. Send any follow-ups due today
3. Send new initial messages (5-10/day)
4. Update status in tracker

### Weekly
1. Review pipeline: how many Sent, Responded, Scheduled, Dead?
2. Identify stuck deals (sent but no response, no follow-up yet)
3. Adjust approach if response rate is low

---

## W03 Execution Plan (Prep Week)

### Day 1-2: Research Blitz
- Go through each company in `00_pending/`
- For each: find contact, research bleeding neck, identify hook
- Update `{company}.md` with findings
- Dump raw research into `full_context.md`
- Mark can share batches with Claude for synthesis help

### Day 3-4: Message Drafting
- Create `outreach.md` for each company
- Draft initial message + 2 follow-ups per contact
- Claude can batch-draft if given the inputs
- Mark reviews and finalizes

### Day 5: Finalize + Tier Classification
- Review all messages
- Classify all 48 companies as Tier 1 or Tier 2 in tracker
- Handle any active inbound
- Ready to send Monday (W04)

---

## Quick Reference: File Locations

| What | Where |
|------|-------|
| Master company list | `data/tracker.csv` |
| Company research (structured) | `company-intel/00_pending/{company}/{company}.md` |
| Company research (raw dump) | `company-intel/00_pending/{company}/full_context.md` |
| Outreach messages & status | `company-intel/00_pending/{company}/outreach.md` |
| Your background/narrative | `ref/mark_profile.md` |
| Claude instructions | `CLAUDE.md` |

---

## How to Use Claude

**Research synthesis:**
> "Here's what I found on [Company]: [paste raw notes]. Help me identify the hook and draft the Your Angle section."

**Message drafting:**
> "Draft an initial outreach message for [Contact] at [Company]. Here's the context: [role, why them, my hook]."

**Follow-up drafting:**
> "Here's my initial message to [Contact]. Draft follow-up 1 and 2."

**Response help:**
> "Got this reply from [Contact]: [paste]. Help me draft a response."

**Call prep:**
> "I have a call with [Contact] at [Company] tomorrow. Pull together the key context and suggest questions to ask."

**Batch operations:**
> "Here are 5 companies with research done. Draft outreach.md for each."
