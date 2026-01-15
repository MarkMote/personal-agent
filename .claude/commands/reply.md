# /reply - Process incoming message

Process a reply or message from a recruiter/contact. Update docs, draft response if needed.

## Input

User provides the message text (copy-pasted from LinkedIn/email). May include sender context.

## Steps

### 1. Identify the opportunity

- Parse sender name and company from message
- Search tracker.csv for matching row (check Company, Contact columns)
- If no match found:
  - Could be new inbound → suggest `/inbound` instead
  - Could be typo/variant → ask user to clarify

### 2. Load context

- Read the company-intel folder for that opportunity
- Check: current status, last action, open questions, conversation history
- Understand where we are in the process

### 3. Analyze the message

Classify what type of message this is:

| Type | Examples | Action |
|------|----------|--------|
| **Scheduling** | "How about Tuesday?" | Draft confirmation |
| **Info request** | "Send your resume" | Draft response + flag what to send |
| **New info** | Comp details, team size, process | Capture in company file |
| **Question** | "Why are you interested?" | Draft thoughtful response |
| **Rejection** | "Moving forward with others" | Update status to closed |
| **Offer/next stage** | "We'd like to extend..." | Flag as high priority, update status |
| **Generic follow-up** | "Checking in" | Assess if worth continuing |

### 4. Update docs

**Always do:**
- Add status line to company .md file: `- YYYY-MM-DD: [what happened]`
- Update tracker.csv if status changed (Status, Next Step, Notes columns)
- Capture any new intel (comp, team, process timeline)

**For rejections:**
- Update tracker Status to "Closed"
- Move company-intel folder to `01_disqualified/`
- No response needed (unless user wants to keep door open)

**For offers/advancement:**
- Update tracker Status to reflect stage
- Flag in company file as priority

### 5. Draft response (if appropriate)

Add to message_draft.md with header:
```
## [Company] - [Action]
**To:** [Contact name]
**Platform:** [LinkedIn/Email]
**Re:** [Role/conversation]
**Date:** [Today]

[Draft message]

---
```

### 6. Update user
Write a breif update explaining the message if necessary, and what you did, and what you suggest. 

**When to draft:**
- Scheduling → confirm time
- Info request → acknowledge + deliver
- Questions → answer
- Positive progression → express interest, confirm next step

**When NOT to draft:**
- Rejections (unless user wants to respond)
- Messages that are purely informational with no action needed

### 6. Summary

Report back:
- What opportunity this was
- What the message means
- What was updated
- Draft status (written or not needed)
- Recommended next action if any

## Rules

- Don't assume — if company/contact unclear, ask
- Preserve optionality — don't burn bridges even on rejections
- Update docs first, then draft — system state matters more than response
- Flag anything unusual for user attention
