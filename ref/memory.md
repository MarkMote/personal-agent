# Session Memory - Running Log

Read this first every session. Short entries only. Detail lives in company intel files and tracker.csv.

---

## 2026-03-04 (Wed) — Latest Session

- **SpaceX deep research completed for HM interview tomorrow (3/5).** Updated full_context.md with: Cole Morgan profile (UW ACL, Acikmeseq lab, trajectory optimization), all active Starlink GNC job postings (general, controls, collision avoidance, nav/OD), expanded Starlink technical details (V2 Mini argon thrusters, V3 specs, orbit lowering campaign, Stargaze SSA system, updated collision avoidance stats), comp deep dive (Glassdoor total $139-227K, Levels.fyi median $167K, equity/IPO context), Redmond culture reviews, and HM interview format expectations.

- **Archer: OFFER RECEIVED.** P4 Staff Autonomy Engineer, $293K TC ($230K base, 10% bonus, $40K/yr equity), $20K relocation, no sign-on. Reports to Dennis. San Jose in-person.
- Mark told Dennis he needs ~2 weeks to see other processes through. Dennis may call Friday Mar 7.
- **Negotiation plan:** (1) Location first -- push for NYC-based with regular travel to SJ. Eddy Yu said location was "not a dealbreaker" in recruiter screen. (2) Sign-on if relocation required. (3) Base bump only with competing leverage.
- **Friday call strategy:** Warm/positive, don't negotiate yet, plant the location seed casually.
- **Ultra: Moved to 03_ACTIVE.** Intro chat scheduled Mar 3, Oliver no-showed. Follow-up email sent. Assessed as T2 (not T1) based on financial risk, lateral skill compounding, lack of passion alignment.
- **Fauna follow-up due today (Mar 3 reminder).** Surfaced to Mark.
- Key context: SpaceX HM interview Mar 5, Anthropic colab Mar 5-6. Archer offer gives leverage.
- Full negotiation tracker at `company-intel/03_ACTIVE/t1_archer-aviation/offer_negotiation.md`.

## 2026-02-24 (Mon, W09)

- **Laurion: Rejected.** Marcus relayed 2/24. Expected after live coding. Moved to 04_closed_lost, tracker updated.
- **Scale AI: Strong pass on tech screen.** Solved both problems, good communication. Prep paid off. Awaiting next steps.
- **Strategic note:** Mark is comfortable extending the search if needed. Each interview improves performance, so longer timeline = better calibration = better outcomes. No urgency to force a suboptimal close.
- **Fauna Robotics: Intro call with Josh Merel (CTO) completed 5pm ET.** Mid vibe, 50-50. Josh focused on Mark's interests, not skills/experience. Said he'd pass notes to team and see if there's a fit. Process slow, ~1 week+. Follow up ~Mar 3 if no response. Full research + technical review docs created in company intel folder.
- **Fauna technical review document built.** Deep dive on ArXiv paper, Merel's 6 key papers, learned locomotion, MuJoCo vs Isaac Sim, compliance/safety, sim-to-real. Saved at `company-intel/03_ACTIVE/t1_fauna-robotics/technical_review.md`. Key finding: Fauna trains in IsaacSim (not MuJoCo despite Merel's DeepMind background). Uses state machine over control modes, not end-to-end. Compliance is software-based (torque limits + trained behavior), not hardware (no SEA/QDD).

## 2026-02-21 (Sat, W08)

- **Archer case study build in progress.** Beamer presentation at `latex/archer_case_study/main.tex`. Template finalized: Tailwind slate+blue colors, TeX Gyre Heros font, custom frametitle with rule, source footnotes with bottom rule.
- Covington GA slide done (map + Archer plant photo). Spec doc: `on_site/case_study_final.md`. Draft notes: `on_site/case_study_draft.md`.
- **Beamer tooling set up:** LaTeX Workshop extension (VS Code preview on save), pdfpc for presenter mode, latexmk installed.
- Saved reusable `latex/beamer_template.tex` and `latex/beamer_design_guide.md`.
- **Radical AI moved to T1** (was T2). Folder renamed.
- **Git:** Set local credentials to personal (marklmote@gmail.com). Pushed to `git@github.com:MarkMote/personal-agent.git`. Added `.gitignore` for large files and LaTeX build artifacts.

## 2026-02-20 (Fri, W08)

- **Viam: Rejected.** Matt Leva email 2/20. "Unique needs of the team at this stage." Moved to 04_closed_lost.
- **SpaceX: Passed recruiter screen → HM interview Thu 3/5 4:00-4:45pm ET w/ Cole Morgan (Sr. GNC Engineer).** 45 min phone. Accomplishment deep-dive + technical. No AI. Cole has been at SpaceX 5.5 yrs, UW MS Aerospace (controls). Mutual connection: Prince Kuevor (Mark knows from Lincoln Lab).
- **Anthropic scheduling:** Requested Thu 3/5 or Fri 3/6 for Colab agent build. SpaceX is 4pm on 3/5, so Anthropic morning would work. No conflict if Anthropic picks 3/5 (only requested 11am-3pm slots).
- **Radical AI: Dave Veisz call went well (2/18).** Good vibe, 40 ppl (37 engineers), 100% in office. Dave putting Mark in touch with Hassan for next steps. Reminder set for 2/24 to nudge if no intro yet.
- Laurion live coding done (11am w/ Yev). Mark expects likely out.
- Created SpaceX briefing doc, Laurion coding prep guide, call prep for recruiter screen.
- **CLAUDE.md updated:** Must read communication_principles.md before drafting any message. Must read reminders.md on session start. Date context updated to W08.
- **Created ref/reminders.md** for date-triggered follow-ups.

## 2026-02-19 (Thu, W08)

- Created prep docs: leetcode.md, scale_ai.md, anthropic_agents.md, robotics.md, gnc.md
- Created 10-day Anthropic agent prep plan in prep/agents/ (SDK, tool use, MCP, workflow patterns)
- Memory/queue/timeline pruned and updated

## 2026-02-18 (Wed, W08)

- **Jane Street: Rejected.** Moved to 04_closed_lost.
- **Anthropic HM screen completed.** Samuel Flamini, went well, advancing. Next: build agent in Colab (45 min, Python SDK).
- **SpaceX interview process researched.** Full write-up in full_context.md.

## 2026-02-13-17 (W07-W08)

- D.E. Shaw Round 1 (2/13): didn't go well. Likely dead.
- Fauna: intro call confirmed Tue 2/24 5pm ET w/ Josh Merel.
- Archer prep plan: Sat 2/21 full day. Case study ~80% of outcome.
- Strategy shift: LC screens are a weakness, pivoting toward builder-friendly processes.

## Key context (persistent)

### Active processes — use folder names for tiers
- **Anthropic (T0):** Colab agent build ~3/5-3/6. Only T0.
- **SpaceX (T1):** HM interview 3/5 w/ Cole Morgan. GNC Starlink, Redmond WA. Top choice if not for relocation.
- **Archer (T1):** Onsite Thu 2/26 San Jose. Case study (safe autonomy/CBF). Flights booked.
- **Fauna (T1):** Josh Merel intro Tue 2/24 5pm ET. NYC. Humanoid robots.
- **Scale AI (T1):** Tech screen Mon 2/24 9:30am ET.
- **D.E. Shaw GenAI (T2):** Likely dead. No official rejection.
- **Laurion (T2):** Live coding done 2/20. Likely out per Mark's read.
- **Radical AI (T2):** Advancing, waiting on Hassan intro.
- **Arena AI:** Stalled, waiting on Brandon.

### Key learnings this session
- **Tier source of truth = folder names**, not tracker.csv. Mark reassesses tiers based on conversations and fit.
- **No fintech at T0** (rule of thumb, not hard rule). Passion-driven.
- **Rejection pattern:** Coding screens are the filter, not fit conversations. Every process where Mark talks to humans about the work is advancing.
- **Pipeline assessment (Feb 20 checkpoint):** 6 real prospects, healthy. No T0s lost (Jane St was T2, Viam/Percepta were T1). Anthropic carrying the T0 weight. 2 of 3 T1s require relocation.

### Key decisions
- Location tier: NYC > SF > international > everything else
- Feb 20 checkpoint: 6 active, stay the course (threshold was 5).
- Hard deadline Mar 10 for new apps to convert by April start.
