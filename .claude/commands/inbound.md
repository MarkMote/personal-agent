# /inbound - Score and respond to inbound opportunities

When the user runs this command, they will paste an inbound message (recruiter outreach, job opportunity, FIR offer, etc.). Your job is to quickly triage it using the established framework.

## Steps

### 1. Read the inbound policy
First, read `ref/inbound_policy.md` to load the scoring framework and response templates.

### 2. Quick Research
Before scoring, gather context:
- **Who's the actual company/fund?** If it's a recruiter, identify who they're recruiting for. Unnamed after multiple messages = yellow flag.
- **Web search:** Company name + "funding" / "team" / "reviews" — use WebSearch tool
- **Already in tracker?** Check `data/tracker.csv` to see if this company is already classified (Tier 0-3)

This prevents wasting time scoring something you'd immediately disqualify with basic research.

### 3. Hard Gate Check
Before scoring, check:
- **NYC-compatible?** Remote-friendly or NYC-based. No relocation required (unless truly exceptional).
- **Not obviously misaligned?** No generic SWE staffing, offshore recruiters, low-signal SaaS, "hustle culture" vibes.

If it fails a hard gate → recommend polite decline, no scoring needed.

### 4. Score on 4 Dimensions (0-2 each)

| Dimension | 2 | 1 | 0 |
|-----------|---|---|---|
| **Skill Compounding** | Robotics/autonomy/controls/simulation | Transferable systems/optimization/quant | Generic software/ops/business |
| **Wealth Upside** | Top quant/breakout startup/big tech senior | Solid but capped | Low comp/equity/growth |
| **Option Value** | Improves elite role/founding credibility | Neutral | Narrows options/pigeonholes |
| **Execution Friction** | Easy convo, low prep, fast signal | Moderate cost | High time sink, long loops |

**Decision threshold:**
- Standard mode: Engage if ≥6/8, or ≥5/8 with at least one dimension scoring 2
- Calibration mode (first 2-3 weeks): Lower to ≥4/8 for practice value

### 5. Strategic Fit Check
Even if it scores well, check against the barbell strategy:
- **Stability/Wealth end:** Top quant, big tech senior, elite AI lab → YES
- **Mission/Equity end:** Robotics/autonomy with real depth, founding-track → YES
- **Mushy middle:** Decent but generic, neither accelerator nor mission → SKEPTICAL

### 6. Output Format

Present your analysis in this format:

```
## Inbound Analysis: [Company/Role]

**Hard Gates:** ✅ Pass / ❌ Fail [reason]

**Scoring:**
| Dimension | Score | Notes |
|-----------|-------|-------|
| Skill Compounding | X | [brief note] |
| Wealth Upside | X | [brief note] |
| Option Value | X | [brief note] |
| Execution Friction | X | [brief note] |
| **Total** | X/8 | |

**Strategic Fit:** [Barbell position - stability end / mission end / mushy middle]

**Recommendation:** [Engage / Engage cautiously / Practice value only / Decline]

**Draft Response:**
> [Response using appropriate template from inbound_policy.md]
```

Important rule for draft: no em dashes. 

### 7. Response Templates (from policy)

**Default (if engaging):**
> Thanks for reaching out. I'm currently exploring senior technical roles in robotics / autonomy / AI systems, primarily NYC-based. If you think there's alignment, I'm happy to do a short intro call to understand the opportunity.

**For Quant:**
> I'm currently focused on robotics / AI roles, but I'm open to selectively exploring quantitative roles with strong technical depth and compensation. If this is in that category, happy to do a quick intro call.

**For FIR:**
> I've previously founded and led startups, so I'm selective about FIR programs. Can you share the fund, check size, partner involvement model, and typical path from FIR to company formation?

**Polite Decline:**
> Thanks for thinking of me. This isn't quite aligned with what I'm focused on right now, but I appreciate you reaching out.

## Notes
- Be direct and concise in the analysis
- If the role is from a company already in the tracker, note its tier
- Fast turnaround matters - don't let inbound create mental overhead
- **Always write the draft response to `message_draft.md`** (prepend to top of file) so user can edit and send without copy-pasting from terminal
