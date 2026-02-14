
## What was the tech

**Backend: process messages and commit to database**
Anytime we get a new message, its classified and routed to one of two agents

Procurement agent:
- Takes info from vendors, structures it and puts it in the database
- Each rate was a table of ~25 fields, with a list of fees, each of which had another 10 fields/fee 
- Hardest part was coming up with a good schema for how exactly we handle rates, given that almost everyone has their own kinds of fees and conventions. 
- We never used it actually, but was also capible of following up with the vendor about missing or unclear info

Why its hard: 
- logic around incoterms and international pricing is complex
- everyone uses their own naming conventions and adds their own fees, in their own language. 
- may send you one rate or hundreds, could be in pdf or message or spreadsheet, you have to handle it all  
- You can't just look through last message, people reference things in previous emails or threads.
- Heavy tail of edge cases. 


Quoting agent:
- More general, connects to database and email, to help answer general questions like "whats the cost of 
- Printing info directly helps with hallucination 
- Simpler: was a react loop with tools and a scratchpad 

Most Complex thing: 
- Getting the procurement agent working correctly was definately the most difficult. I mean there were just so many edge cases, and updates we had to do to our schema over time. 
- For example, in the early days, we found out that certain chinese characters were causing code to crash
- Later on it was more things like: Oh, this carrier offers time dependent fees in their rates, with a peak system surcharge 
- Handling different kinds of fees in a structured way was definately a huge challange. 


Key to solving this: 
- We built a good operator dashboard on the frontend 
- Agent gives a confidence score, and you can review
- Anytime you see a new fee, add it to the database
- Anytime you see an error or mistake, you can feed it back with instructions, or spin up an api on localhost and begin patching the code. 


## Procurement Agent Workflow 
- Wrapper around agent: Pulls in the message, the recent message history with this person, any memories you have saved on the sender and their company
- Quick classification to make sure this is something we actually need to pay attention to
- Initialize context and scratch pad. 
    - Do i just need to focus on the current message or something deeper in the history
    - Summary of relevant conversation clipped 
- Make a plan: do i want to add new rates, respond or do nothing. 
- Pass the information to a rate extraction workflow 
    - combines emails and documents
    - identifies what parts can be done programmatically, often with reflection and reties
    - does standardization and matching with SSOT
    - notes where it found rate and any concerns for audit purposes 
    - gives a confidence
    - gives a summary to the operator on how the process went. 
    - logs steps for debugging. 
- Sends the info back to the wrapper 
