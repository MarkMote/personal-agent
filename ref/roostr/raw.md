## Roostr 
To be honest, i joined this because i beleived inthe cofounder. 
After we decided to shut down Pytheia, i knew two friends with startups
- Jacky @ roostr: working on automating weekly business reviews 
- corbin @ artifact.engineer: working on building coding agents and a design automation software for engineering software development "now pitched as "# The Design Tool for Electrical Systems - Artifact is a collaborative, version-controlled, and multi-layered ECAD tool. It organizes interdependencies between sub-systems and generates harness drawings, pin-tables, and BOMs real-time"
Corbin was working in an area i cared about, but I honestly wasnt convinced of his ability as much as jackys, i choose to prioritize team over idea. Plus Jacky and i both had this crazy idea of getting an LLM to run your startup. We wanted to see if it could be done, how much it could be done.  
Part 1: finding levers
Jacky and i made our first sale right after i joined. Was ~24k ARR automated weekly business review for a freight forwarder, Nowports. At first it was just a "connect to your database and automate the weekly business review in google sheets - tracking all metrics". We developed this idea by having llms sort through the data, do data analysis, and write executive summary on the business as a whole. These were one paged linked reports that told customers how they were doing on metrics and dug into the exact root cause: we mapped out the funnel as a graph, the metrics that defined the funnel, and had llms investigate causal relationships. Final report was in google docs (their preference not ours). It was all created with a single script. They really liked this, in fact the CEO liked it so much he started setting up weekly meetings with us so that he could pick our brains on the company, this lasted for a month or so. 
We also learned something critical about their business: it was just one primary lever that was influencing all the quotes: fast quotes. The problem we noticed that this industry was very far behind. they managed quotes in a google sheet or their own personal email, vendors sent them rates via email in a messy form, if they were really on top of things they would organize into a google sheet, so that when they got a rate request, they could actually get back to the person in a couple hours. It should have been very simple, like tech from 20 years ago could have solved it, at least in terms of a manual solution with a database, but they couldn't figure it out and it was costing them big.  This was a unicorn company by the way. 
Why this first part was interesting to me: intellectual curiosity about how many real insights llms could reasonably bring to a business. could an llm run a business, which parts coudl they excel at?  which parts would humans still excel at. it was both the excitement of building llm based systems to solve and automate real problems but also I find business itself to be a kind of engineering problem. I think the best euntrepreneurs do. So it was also an exceptional opportunity to find the boundaries of what was possible with current tech. Additionally, digging into a real business like this, making it your primary goal to find their inefficiencies and problems initially seemed like it would be an ideal way to surface real issues down the road. 
Why we didnt sell more at this phase: 
- heavy building 
- ai saas fatigue. though we had a different appreoach and philosophy, there were a lot of companies in AI-BI-SaaS at that time, so there was skepticism. we never successfully figured out how to escape competition with the initial idea. 
My role throughout roostr has been to build, and jackys to sell. He prototypes, and i make pitchdecks and marketing materials, we both oversee direction, but this was definately a highly technical role for me, compared to pytheia. 
More about the tech: 
- Every week a cronjob would run that pulled data from database and turned this into google sheets and google docs. full process automated. all the content was linked, and heirarchical. for example the business summary doc was a one pager on the entire business, that would list root causes (think 6 sigma rca applied to business metrics) and link to more detailed reports, as well as the google sheet with the data. 
- A frontend would not have been hard to make, but they liked the familiarity with google ecosystem and its features. beset to meet them where they are and focus on what they actually want ather than whats flashy.
- connect to snowflake database with python connector 
- pull in all data to pandas
- do traditional structured data processing: create metrics, turn metrics into time series, extract signal from noise, figure out current growth trajectory using things like prophet, and gaussian process models. Analyze with logic and statistics. This would all be put in markdown files
- Then llms would turn the raw data and analytics into reports a google sheet. there was basic summarization, but also the ability to search agentically, as with 100s of metrics the context was massive. 

Part 2: building better levers 
They wanted more and we had ideas. We were in talks with them about moving to the next stage, a 20k/month contract for a rate management system. We could give them something that solved this right. so not only do they manage and keep track of the rates, but they are not spending
We proposed an ai agent that would connect to their email, automatically process the rates with llms, just letting them review and approve, then commit to their database. As a starter they could manually upload and we ould get the manageent and rate search engine the them in ~3 weeks, which we successfully built while still negotiating. 
The full system would: 
- connect to all their emails (using Nylas, making it simple to set up)
- recognize when someone was sending them rates
- extract the rates in any form, which is very non-trivial. freight forwarding has a lot of different kinds of conventions and rules, for example you need to match exactly to an existing set of ports, you need to understand and process incoterms, all the different fees and so on. The simplest form of this just capturing rates and pol, pod, storingthe rest as metadata. Even that is suprisingly ocmplex because of all the different ways people send you rates: sometimes emial, sometimes another language, sometimes long excel file, all with different conventions. 
- store the rates as pending in a database, we used mongo
- Create a frontend for this that allowed the operators at their company to log in, see the pending rates and audit them (if they wanted to) by comparing the rates to the email: ie you open an emial and see all the rates, or in another view, click on a rate to see the source email. The human reviewer commits pending rates to accepted status, and they become searchable on another page. 
We eventually built all of this

Note: they had previously had their company spend 6 months developing something similar to this, a most basic version, before they eventually scrapped the project. They could not deliver a result on this. We built a working MVP (100% built by me) in 1 month, and refined it with failure cases over following months. Fees were not initially integrated into the data, but the main fields were. 

What happened: we were in negotiations, we had our internal champion and they liked the price. We had a few weeks of the talks, which was enough time for me to build a working prototype. They admitted it was better than what they had spent 6 months on. We were able to make a really good case for how much money it would save them, which was a lot, because we had access to all their data and metrics from our first product. Then the division became under new management. A very old-school anti-tech person came in, scrapped this and other things they were working on. They doubled down on the current process of slow quotes and outsourced labor. 

Why this part of roostr was was interesting to me: very high impact on the business, very practical real world application of llms. would have been using them at a scale almost no oneelsewas at that points (this was all around december 2024, a year ago). And most importantly there was a huge need it seemed. 


Nowports cancelled the project, but we were sitting on something we knew had a ton of value, and that we had technically derisked and proven was possible: we could build it, we could make it work, others tried and failed. We identified this as the main lever in freight forwarding, and had an automated way to pull it. 

We were almost dead in january 2025, the contract was cancelled, we were out of money. We gave it 3 additional weeks to get our heads above water, and sell what we had started building as a saas to other freight forwarders. if we couldnt make a sell, we would shut down. I rapidly built and jacky rapidly prospected. We sold together on the calls. We got our first 2k/month customer 2 weeks later (a tenth of the nowports price, but it was soemthing). We used that to raise enough investment to carry out the experiment: just 225k for 9 months of runway. I have always been against raising unless absolutely necessary, in hindsight this may have been a repeaed mistake. we landed a couple other contracts in the next 2 months, being fully integrated with one person and having 50k/year in run rate from contracts with thisand two other customers.  but we realized something:
1) it worked: once fully integrated with our first customer, he made an *additional* million in sales the first month of being on the system (revenue i beleive) a significant increase for a small forwarder. 
2) there was massive upside to it working, and we would not capture that at. we made our customer a million (less in profit since freight has large pass through, but still substantial) but we made 2k. Even knowing the lift it would be hard to sell enough to really get the upside here. 
3) there was friction: the rate thing worked well but anything we did would be fighting an existing process. The typical process, especially for small forwarders, did not involve fast quotes. They liked to search through their emails once they got a quote, and the obvious ai solution that would fit into their system, would not be to collect the rates in advance but to have a bot search through and reply to emails. Its a local optimum problem, and the same one places like Flexport goes through with the little ai they actually do: you can get a benifet from incorportating ai into your existing workflow. its a harder and much less effective solution than redefining the workflows to be ai-first. People want things their current employees know how to do, and that fits their existing system. Thats reasonable, and logically, but if you actually had a freight forwarder, that was designed from the ground up to be agentic, to keep track of all the data at a more detailed level than in an operators head and in google docs, if you did the hard processing problems in advance and were meticulous about data and structure, you could be insanely efficient. Procurement and quoting is 40-60% of operating expenses, but the other problems worked this way too. Freight ai has become really hot, because it works, but everyone is doing this move of saleing saas tools to forwarders, ultimately a losing game. not to mention the integration problem of not owning the full stack, having to work in a frankenstein stack of other saas tools. 
4) No one was building an AI-native freight forwarder. You had mom and pops, and you had the 2010s era digital freight forwarders like flexport and nowports (who we worked with), whose stated preferences were ai automation, and gladly sold that narrative, but whose revealed preferences were more outsourcing. We saw the inside of one large freight forwarder, we could see other evidence from flexport: jobs they were hiring for, who was acutally on their teams, etc. they were not hiring ai engineers, they were ramping up their operations in south america and the phillipines. jacky was exflexport so we also had a massive network of poeple who worked there to validate this hypothesis, including ex c-level people at the company. 
5) because of the above there was a massive delta in public perception and investor perception. Not only is freight-forwarding a trillion dollar industry that has remained massively fragmented, not only did llms provide amazing tech enablement, but there wasn't a single serious ai player. people thought people were doing it. people claimed to be doing it on their sites, but they were just doing the very logical thing of doing what worked for their own business model, a la innovators dillemma. (none the less freight forwarding remained toxic to investors because of a decade or two of burned automation promises). We had a true, meaningful answer to the thiel question, we had a way to build a flywheel and a monopoly if it worked. 
So of course we pivoted. We knew it would be hard. We knew it would be a huge bet. But we didnt get into startups to play it safe, this could have been one of the largest consolidation opportunities ever. its a once in a century perfect storm of tech enablement, fragmentation, real need from a stable business and outdated industry. It could truly change the world if it worked.


Part 3: pulling the levers
We decided to execute on being a freight forwarder may 2025. We would use and develop our own tech, for our own use, to change this very old outdated business model. 
We had the procurement engine that worked, we would automate one step at a time, chunking away, having extreme efficiency. 
But the start was very slow. The tech worked but gaining customers was hard. You could undercut flexport and every other forwarder on price, but that wasnt enough of a value prop to get people to switch from the guy they trusted. Contracts in this area dont have a lot of churn, people have their guy that they trust and getting them to switch is non-trivial.
So we spent months focusing on outreach, we knew it would be difficult, so we focused a lot on sales, the real bottleneck. I developed software to connect to import yeti and generate a targeted webpage for each prospect automatically: this is where and what you ship, these are the tradelanes roostr has rates on, this is how much we can save you and so on. 
We also developed a dashboard and tracking system: think: turn the whole process into a finite state machine, and have specifized agents be in charge of managing the graph, one node at a time. start manual, add automation. in principle, agents could control the entire process, only having humans step in for review and edgecases. We worked with Grace Sun, ex flexport and amazon, to develop a standard operating procedure: we couldnt win on just price so we had to win on reduced friction and better trust as well, eliminating human errors in the process. 
we didnt get our first sale until November. But since then we have gathered over 100k in run rate. We have hired an sde in phillipines to help with the work and keep things less manual (in traditional freight forwarding style), but are also relying on our tech heavily. 


Now:
- We are going to seek investment in the background
- If not we are going to convert the business to passive income
- Jacky may continue, I will likely leave. 
- We grew it to a point where its giving returns, and where we can have it operate while we move on to others. 
- out of money, need to look for a job. We found something useful, but its a slow business, and we couldnt beat the clock
- on the other hand, feel like its time to move back to an area im more passionate in. I have always loved space, its deeply fulfilling. Aeronautics for similar but lesser reasons that astronautics. Robotics as well. Its the next big thing. it will change the world like nothing else and im in a unique position to be a part of that revolution. 
- Freight forwarding works. Its not a rocketship, but a spaceelevator, or at least a hot air balloon. 
- skills i think i developed well: 
	- product design
	- the "meta-engineering problem": figuring out what needsto be built not just how to build it. Whats important, how to iterate, how to experiement. 
		- I personally beleive there is a heirarchy: knowledge < intuition < taste. In this area i think ive developed taste. 
	- but also how to build it. the full system, the full stack. From design to used by customers. 
	- general, messy, real world, poorly defined problem solving. embracing the chaos. 
	- communication: working with people in stressful scenarios, a relentless pursuit of results over feelings, while also staying cognizant that we are emotional and very human creatures. 
	- Systems thinking and big picture thinking 
	- frankly just getting things done. between phd, 2 startups, and llms, i feel like i have the skills to solve any problem
	- creativity and other results of breadth not depth of experience
	- design and frontends. Fun, and i can do it well. but not challenging in the right way. 
- never cracked as well as i would have liked
	- sales and distribution. Talking to people is great, but sales is mostly emails and prospecting. I also possibly have maladaptive honesty. I am a great engineer because i realize things are never good enough, the same quality adds barriers to sales.  
	- getting investors excited, at least about the current idea. The few investors we talked to at pytheia seemed to resonate with the idea, but we chose to bootstrap. 
	- With respect to the above, i never became great, but i did study and execute and pull of more than 99% of engineers. 
	- because of above ill probably be swimming upsteam in interviews. i beleive in show dont tell, but interviews are all tell. And in technical interviews i have always proritized first principles problem solving over memorized quick thinking. Its worked both ways for the few internship interviews ive done. If the questions are hard and messy and undefined i do great, if its coding or a lot of the ismple more straightforward things ive always failled to excel. People work with me they love me, but there is an obvious gap here in ability to sell myself, so your help would be appreciated :)

Ok lets properly finish roostr story
## Roostr Q&A
Backend Stack: all products
- written in python, packed in docker, deployed on digital ocean. 
	- justiication: python great wrapper language. digital ocean cheapest that met our needs. Slightly more complex than some of the other options, but i wanted to use it as an opportunity to learn more about how things worked (given it wouldnt be a big time cost) being my first backend, extra control ould ocme in handy, and it would likely be easy to port if we ever needed to. 
- Write very modular code with unit tests for each module. each file has a common sense smoke test and modules have unit tests. Use github actions to test on push. tests are easy and can be ai generated so why not use a lot of them. 
- Very strict about types and interfaces, each module a black box with very careful attention paid to inputs and outputs. allows modularity. 
- NOTE: for more info about style and approach, ill paste in my code style guide
Frontend: 
- We used nextjs (react+tailwind) and deployed on vercel. 
	- why? nextjs makes frontend easy. They optimize for things we wouldnt otherwise have time to optimize (be good if you could help me be more specific aout this). Allowed us to have something nice and quick. The particular kind of site wouldnt have an extreme amount of usage per what we were getting paid, such as compared to consumer apps, so vercel strongly made sense. 
- Three sights: marketing website is shiproostr.com, application 
Data layer: 
- mongodb. Good when you iterate on your schema a lot. did prefer generally flat structure to make future migrations easier. 
LLMs for development:
- before cursor and claude code: wrote scripts that would convert data layer and specific files to markdown files. 
- after: claude code with mcp server for mongodb and playwrite to iterate on frontend or go to websites. Occasionally a bash script for orchestrration. Subagents and slash commands but those are standard. Type definitions treated like contracts for modules and llms required to create and use unit tests for everythng it makes. 
LLMs for product. 
- Experimented with using sandboxed claude code as primary agent in data extraction (ie run as part of look in script in headless mode). was fairly good for general tasks like the quoting agent we built, a little less good for data extraction where we did need specific llm logic for different kinds of things we saw. 
- Both quoting agent and data extraction agent used a custom agent pipeline we build. ie run loops, call these subagents, do this logic, call these tools. clean date programatically as final stage. offload certain things to tools when possible: e.g. if we get a large excel file with 100s or rows, would not want to just throw an llm at it. do want to use an llm to interpret the column meanings then python to turn that into a csv or pandas, then clean data (e.g. map to standard pol pod codes) with either logic or llms when cant do programatically. allowed us to do a lot with little cost. 
- Didn't use langchain, probably need to justify that somehow but just didnt really need it when could use tools in claude directly, and make my own custom classes for llm wrappers. in hindsight, there was probably some vendor lock in.
Quantification and other
- Started Roostr April 2024
- WBR: 
	- just nowports using
	- 2 weeks to mvp, which was just the google sheet automation 
	- 3-6 months with additional building agentic systems and insights around it
	- possible mistake made: should have built a frontend. our customers did not want one, and preferred google sheets, but the lack of at least a little bit of flashyness hurt sales pipeline i think. especially since frontned so easy.  
	- maybe 50 ppl in the org, the CEO was reading directly
- stage 2: freight saas: 
	- 3 customers, 1 fully integrated, 2 in light usage phase. contracts signed, 60k run rate on these contracts before deciding to pivot. We made 60k in 8 weeks before buckling down on building and excecuting to make customers happy. 
- exact numbers in the screenshots i gave. the wbr stat is a big misleading since we only had once customer
- stage 3: 
	- since november ~ 2months, we got to 100+ k runrate across two customers: a startup and a small importer. vast majority is coming from startup
	- We are not getting inbound. Approx 1 person a week. havent landed inbound yet but its a good sign. 
	- cost savings: undercutting flexport and other big people by 10%. Getting rates witha combo of people sending us rates and just doing the scrappy thing of scaping flexport and finding way to honor it after. could lose money on this, but LTV of cusotmer more important. 
- Lines of code and all that, just see my note below about askingthe coding agent. can give all details on products. 

Other: 

- We did 2 things: did have a golden dataset of around 20 examples that represented different types of emails we would get, or would be particularly challenging, ran on major updates. When we were selling it as a saas, we ran on major updates, and example set may have even been smaller abck then, because there was a cost to getting it wrong. With 3 customers, we could just be on top of logging into their accounts and monitoring manually. It only broke once or twice, but we realized before the customer did. 
- Once we were our own freight forwarder, we could relax a lot on testing, if we needed to. what we did was designed a better system rather than just designing the system better, it was one of main benefits of switching to being our own forwarder. Once we became our own forwarder, i was personally reponsible for improving the rate managment flow. 
- In both cases: pattern was: any failed extraction from our rate extractor, any time if messed up, couldnt handle or got something wrong, we would fix it on the fly. Sometimes this was a bug (e.g. certain chinese characters in xls files would break it) sometimes this meant creating a new module. Then we would take the example that broke it and add the id to the test set. Effectively a zero tolerance for long term error policy. 
- Most frequent fix was actually just adding to context and data. obscure ports, inco term subtletys, obscure terms used in the emails. 
- Big picture is that I designed the tool not just to work well on autopilot, but to have a quick reaction and improvement loop so we could react when things werent perfect. This is essentially the spacex strategy: instead of spending 10 years trying to proactively solve every issue, you launch the rocket, occasionally blow it up and fix that. In the end you spent your time on what was actually the problem. I had my own custom tool for iterating with the rate extractor agent. as soon as we got an error, i could pull that tool up in 1 minute and begin iterating on the code. Its not a universally right thing to do, but it does maximize speed and improvement over a given time. These are the tradeoffs you need to make in a start up and it was 100% right for us. 
- extra 1M in revunue: dont know for sure, but safe to assume 5-10% of that was profit 
- Cost to serve was very small. Since we combined llms with programmatic tools, large documents were actually cheaper sometimes. e.g. long xls was about mapping column and sheet names to known fields, then turning over to loop in python. 
- specifically: maybe <1cent-10cent per rates email. would get between 1 and 1k+ rates per email
- we used different models for different tasks. smaller models would do the classification of the email intent for example, and whether it even had rates. 
- So at a few relevant emails a day, we are talking less than 100 per month per customer. 
- your answer on langchain is good. it came down to having full control. 

