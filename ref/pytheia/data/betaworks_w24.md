Info:
NYC 
Feb-May 2024 
500k 
Priority deadline: 12/29 
Final deadline: 1/12 

Optional to do: 
Make demo site 
Make landing page 

Company Name 

Website *
pytheia.com 
→ redirect and make demo 


Describe your product *
In 1-2 sentences, tell us what you're working on and why it matters. 
We’re building a software service to help manufacturers predict trends in consumer demand and plan production. Covid exposed major production planning problems in the RV and Marine industries. We believe we can use agents to help manufacturers plan production more accurately and at a lower cost.

We’re building a software service that will help manufacturers figure out what to produce by understanding and predicting trends in consumer demand. We do this by using agents to collect and analyze inventory and pricing data from the web. 

Video introduction *
Please link a short 1-2min video of your team, introducing yourself and giving us a demo of your product if possible. Any link (YT, Notion, Drive) works for us.

Hi I’m Mark, 
I’m Matt, 
And I’m Ben
We’re Pytheia. 
We’re building AI to help manufacturers plan production by understanding and predicting consumer demand. 
Agents help us collect and analyze pricing and inventory data from the web, 
We present it to customers as an online dashboard 
We started on the idea in July
Began bootstrapping by selling data in October, which led us to our first enterprise customer, and brought us to over 25k/month in customer billings. 
The three of us met 5 years ago in grad school. 
We’ve lived, studied, and worked together.  
And we’ve built and launched several products together. 
Collectively, we also a strong technical background with 2 PhDs 4 masters degrees, and over 1k citations from our academic research 
OK, lets check out the dashboard. 
<Cut to video Matt makes going over dashboard and maybe some of the tech/code> 



What's your definition of an AI agent? *
An AI agent is created when one or more LLM models are interconnected within a feedback loop.  Interconnecting LLMs allows for separating reasoning and action, and can create specialized components from generically trained LLM models.   This also facilitates using non-ai tools within the overall architecture, allowing the AI to handle more complex tasks. 


An AI agent is created when you place a feedback loop around an LLM. 
Feedback allows the LLM system to perform more complex tasks by autonomously observing, learning, and iterating from the results of previous actions. 



Their definition: [from this]
Our next AI Camp is focused on agents and the technology that both enables their creation and ensures they fulfill your/their goals. What defines an agent? In our view, an AI Agent can:
1. Perceive, synthesize, and remember its context;
2. Independently plan a set of actions toward an abstract goal;
3. Use the tools necessary to execute against that goal without human support; and
4. Evaluate the results of its work against the overarching goal.
Modern LLMs need to be enhanced in each of the dimensions of the above definition, and those enhancements will probably arise from infrastructural/framework unlocks, rather than purely adding more training data or model parameters. While the hype on agents has gone up and down for close to 25 years, we now see that the infrastructure is currently being built, such that the moment for agentic applications and software is coming.



Are you working on an agent or infrastructure/tooling for agents? Both are ok. *
Describe the parts of your product that are agentic or support agentic behavior.
We’re working on two agents: one for data sourcing and one to facilitate customer interaction with the data. The data sourcing agent writes web scraper executables, and maintains the infrastructure around the data that is produced. The customer facing agent is an assistant akin to code interpreter with access to higher level primitives related specifically to our problem domain and dataset.

We’re working on an agent. Our usage falls into two categories: data sourcing and customer facing. The data sourcing  used to collect data via web scraping, and to create and maintain the infrastructure around that data.. The customer facing is an assistant akin to code interpreter with access to higher level primitives related specifically to our problem domain and dataset.

What's the technical stack? *
Explain in as much detail how your product works and the various models, middleware, and tools you use

We are mainly working with GPT-3.5-turbo-16k and GPT-3.5-turbo-instruct from OpenAI. We have also experimented with local models like the Llama 2 family and Mistral. We occasionally use AutoGPT as a base-layer agent due to the robustness of its tool calling, however, our primary agent infrastructure is custom and supported by tools including Langchain and ChromaDB. We’ve also developed some internal tooling similar to Microsoft’s autogen that we use extensively in the data sourcing agent. 
The user dashboard is a Next.js app with FastAPI, typescript, and tailwind css. We use the Apache Superset for data visualization. 
All code was written by the founders. 

For LLM models, we use OpenAI Models such as GPT-3.5-turbo-16k and GPT-3.5-turbo-instruct. Additionally, we have experimented with local models like the llama 2 family and Mistral. The agent infrastructure is supported by tools including Langchain and ChromaDB. We occasionally use AutoGPT as a base-layer agent due to the robustness of its tool calling. We’ve also developed some internal tooling similar to Microsoft’s autogen that we use extensively in the data sourcing agent. 
[TODO: explain how this is being used in more detail, how the stuff is used, where agents come in]
The user dashboard is a Next.js app with FastAPI, typescript, and tailwind css. We use the Apache Superset for data visualization. 
All code was written by the founders. 



Any other relevant links (deck/demo/alpha/testflight/github/etc.)
Share any links that can give us a sense of your product.
https://garlic-ashen.vercel.app 
---> make demo repo?


Prior funding *
Have you raised any prior funding via investment or grant programs? From Funds or Angels?
In Spring 2023, we took part in the Pioneer Accelerator program led by Daniel Gross. As part of the deal, Pioneer owns 2% equity. We have received no other outside funding. 

Origin story & Bios *
Tell us any relevant information about how your company/product was born and share your team bios. *Please include links to LinkedIn profiles*
How we all met and started Pytheia: 
The Pytheia Co-Founders are Mark, Matt, and Ben. We all met in a Robotics research lab at Georgia Tech in 2018. We worked on several projects together and moved in together in January 2021, while still in grad-school. We launched in late 2021 and all became full time by July 2022. We initially worked in the area of robotic perception, launching and iterating on several different products. We began experimenting with agents and LLMs in the spring of 2023 before pivoting to the current direction in July. 

Progress: 
We started on this direction in July 2023. Initially we focused on pricing optimization (with data collected on the web through agents) before finding the bigger problem of predicting demand for supply chains. We began selling data in October as a way of bootstrapping while we began to build out the technology. We got our first enterprise contract in November. We’re currently over $25k MRR in subscription sales. 

Mark Bio: 
Mark Mote has a Ph.D. in Robotics and a M.S. degree in Aerospace Engineering from the Georgia Institute of Technology. His Ph.D. research was on autonomous robotics, spacecraft, and optimization. He has 800+ citations from research publications in these areas. Additionally, he has worked in research and internship positions with Stanford University, the King Abdullah University of Science and Technology (KAUST), École Nationale Supérieure de Mécanique et d’Aérotechnique Poitiers Futuroscope (ISAE-ENSMA), MIT’s Lincoln Laboratory, NASA’s Jet Propulsion Laboratory (JPL), and the Air Force Research Laboratory (AFRL). 

Matt Bio: 
Matthew Abate has Ph.D. in Robotics from the Georgia Institute of Technology, along with M.S. degrees in Computer Engineering and in Electrical Engineering from the same institution. His Ph.D. research was on applied applied mathematics and efficient computational prediction methods. 

Ben Bio: 
Ben Mains holds an M.S. in Electrical and Computer Engineering from Georgia Tech. His background is in software development and computational techniques for scheduling tasks in distributed systems. He has production-level software development for autonomous marine vehicles at Yamaha. Additionally, he has experience at General Atomics, Inria, and Raytheon. 

Links: 
Mark LinkedIn:  https://www.linkedin.com/in/mark-mote-86bb25215/ 
Matt LinkedIn: https://www.linkedin.com/in/matt-abate-9919b1a8/ 
Ben LinkedIn: https://www.linkedin.com/in/johnbmains/ 
Mark Personal Website: https://www.markmote.com/ 
Matt Personal Website: https://mattabate.com/ 


Team Size *
Pytheia has 3 Co-Founders: Mark, Matt, and Ben. We have no other employees. 

Team location (if remote, please indicate). *
We’re currently based in Atlanta but planning to move to either New York or San Francisco in early 2024. 

Favorite Agent? *
Tell us about your favorite example of agentic software (other than what you're working on).
I don’t believe it’s being worked on anymore, but the smol-ai developer due to the simplicity and efficacy (at the time of launch) in comparison to other efforts.



Agent/ Product Specific Questions
How have you used agents in the past?  matt
Beamergen and webscraping 

How are you using agents now?  ben
Not 

How are you planning to use agents in the future?   mark
We’d like to use agents for a user-facing assistant, and as a way of building, monitoring, and repairing the data pipeline. 

Timeline of the Dashboard so far?    mark
Got the customer in November 
Built it in December 
Released it in January 
Hoping to get our second enterprise sell in February.

What’s on the roadmap? What new features are you hoping to add?   unassigned
Better visualizations to capture demand. Its something we intend to iterate with, but there’s a lot more to show in terms of visualizing what’s selling and where. 
Alerts feed: twitter style feed with AI generated reports on whats going on day-to-day
Automated reports
Build up the chat interface (see below) 
Long run: integrate user data to get recommendations on what to produce and how to price 

Do you foresee a consumer-facing side of this tech?  mark
Yes! Possibly through a freemium tier, we’re very excited about building a knowledge engine that users can chat with. 
Imagine Perplexity or ChatGPT, but with the webs information already cached, structured, and analyzed. 
It could act as a personal analyst, or produce a personalized McKinsey style report based on your prompts. 
We’re including the chat interface in the product from the start, so that we can iterate with this.

Favorite Paper?   ben
chain of thought paper 

Most Important Questions

Tell me about the idea? mark
Pytheia helps manufacturers plan production
We do this by building AI that collects data from the web 
and turns it into insights on consumer demand
..
Further 
So In order to understand what to produce, suppliers need to understand what people are going to be buying downstream. 
We help them figure it out by aggregating and analyzing data from the web. 
For example, say you want to produce parts for marine vehicles.
We’d get our software look at the listings for all marine dealerships across the US, gather the price and status of the listings, and then extract the major insights, such as: 
Are dealerships low on inventory
What’s selling best
etc. 

Tell me about Pythiea? (history of the company)  mark
We all met about 5 years ago in grad school. 
We started about 2 years ago we moved in together and initially started Pytheia  with the idea of using traffic cameras to help autonomous vehicles
Since then we iterated through various AI as a service products before eventually finding our current direction this past july 
At the time we all became really intrigued by LLMs, and realized to potential ….

Can you tell me a little about the team? matt
We’re all technical.  Mark and I also do sales. 

What problem are you solving? mark
We help manufacturers understand consumer demand so that they can more efficiently plan production. 
Imagine you’re in charge of making parts for some kind of vehicle. 
You need to figure out the type and quantity of parts to produce. 
But the problem is that you don’t have a good view on whats going on downstream: whats selling, how well stocked the dealerships are, and do on 
This is where we come in. We scrape the internet and make sense of the data. 


Who is the (ideal) customer?  mark
Tier-1 vehicle suppliers. 
Ideal customer is a company that needs to understand demand from pricing or inventory information on the web


Why now?  mark
A lot of the data 
LLMs are allowing us to come in and structure this data. 
With the right technology can replace teams of analysts with teams of agents. 

Why you? What’s your unfair advantage?  matt
Good technical background needed to execute 

How big is this market? How will it grow. ben
RVs (Mobile Homes): 30B * 0.004 = 120M
Other Recreational and Outdoor Vehicles (Marine, RV, Moto, ATV, similar): 100B total -> 360M
Construction and farm equipment: 200B -> 720M
Auto:  650B -> 2.6B
Rough total manufacturing: 1T -> 4B
Total average CAGR ~8%

How do you get to 100M ARR?  ben
Doable cornering the Recreational and outdoor vehicle market. 
NOTE: At current pricing, would need 1000 customers or to raise prices.

What’s your traction so far?   matt
3 customers. One in the main area, two in a similar area back when we were focusing on pricing. 

What’s your go to market strategy? ben
RVs -> Marine -> Other Recreational Vehicle
Approach auto once proven in RV
Upsell production planning 
Already have customer in RVs, relatively well connected in Marine due to previous work experience

Can you tell me about your current customers?    mark
.



Potential pushback 
This looks like consulting?


Do you really need agents for this? 





Other Questions 

Can you give me a brief explanation of your project?  mark
We’re building an AI analyst to help manufacturers plan production. 
In order to understand what to produce, suppliers need to understand what people are going to be buying downstream. 
We help them figure it out by aggregating and analyzing data from the web. 

What have you built so far?  ben
Dashboard for customers
Viz
Chat
Download
Internal tooling for data collection
Normal stuff + some agents


Why is no one else doing it?  unassigned
Data on web
Some doing it, but not in scalable way
Doing it at scale requires LLMs. 
Theres also a technical barrier in that doing it well involves a lot of math and data science knowledge. 

How did you pick this idea to work on?  ben
We started playing around with LLMs this summer and initially had the idea of using agents to scrape the web so that we could help businesses figure out price. 
We got a couple customers here, but discovered pricing itself wasn’t that sticky, but there was a much bigger problem adjacent to it with the inventory. 

How long have you been at this? How are things going with the project lately? matt
Started in July, came on current version of idea in November 

Insights? What do you know that others don’t? unassigned
Did a lot of previous work on modeling and prediction problems 
Lot of technical analogs to robotics 

What’s the rocket science here? (similar to below question) ben 
Predicting demand accurately and managing the data sourcing for that demand

Who will be your next customer? mark
Right now we’re focusing on tier 1 suppliers for marine vehicles. 
They have a similar structure and problem as the people we’re currently working with,
Also Ben has connections and domain knowledge from his time at Yamaha. 

How do you know people want what you're making? matt
Lippert bought it 
Nothing to indicate anything anomalous about their situation 
Also spoke with Yamaha, and they confirmed that they had the problem. 

How does this become a billion dollar company? ben
[Equivalent to the 100M ARR question]

How did you decide to start working on this? matt
Initially excited by LLMs 
Saw opportunity based on webscraping and data science 
Talked to customers and iterated until we found the thing that people really needed

How will you get users? matt
Initially: Outbound sales and network 
Then: 

What's a key thing about your field that outsiders don’t understand? mark
don't have downstream info on whats selling 

What are some of the weird things you worked on or you've done in life? matt
beamergen 

Who are your competitors? mark
Most similar is arena AI, but they’re mainly focusing on CPG
A lot of the work is being done by consultants and internal teams, but we think that we can use agents to automate what’s being done here. 

Who’s doing similar stuff? Why is no one else doing this exact thing? mark
A lot of the work is being done by consultants and internal teams, but we think that we can use agents to automate what’s being done by these groups. 

What’s new about what you’re making? ben
Previously, there was not use of fine-grained, real-time inventory data for forecasting and production planning

What are your weaknesses and how do you plan to work around them? mark
Lack of network and domain knowledge is a weakness 
Think we can get around the network problem by going to trade shows and possibly finding targeted advisors 
Heavily emphasizing customer conversations to get to speed on domain knowledge 

How are people solving the problem today? ben
Consultants and internal teams 

Do you have customers/ traction? matt
Yes. 3 Customers. One is 25k/month and in the main area
The other two are 1k/month combined. We acquired these at the time when we were only selling data.  

Are you using hardware? ben
No 

Who needs what you’re making? matt
Most immediately: Tier 1 suppliers for vehicles
Down the road: Any manufacturers 

What's your timeline over the next year?  matt
Jan: get product to useful state with demo 

What’s your biggest problem now?  mark
Getting the second sale. 

I see you did Pioneer. What did you learn from Pioneer?  ben
Iteration speed, engagement, and feedback is important


What kind of success did you have pre-pivot? Did you have revenue? Why did you pivot?  ben
At the end we were using cameras in restaurants
Thought about using AI (with recent developments) in other ways to help them


What did you do in the first two years?  matt
Failed, explored, pivoted, explored, landed sales - have a plan where to go from here

What’s your moat?  mark
Primarily data: live data, historical data, and eventually customer data. 

Who are your customers? How are they different? (market segmentation)  ben
Rvs. Soon to be marine. T1 and OEM. T1 larger than OEM and more disconnected.

Who is your ideal customer?  ben
Data team manager at a T1 supplier for Outdoor and Recreational vehicles

What’s been your biggest challenge with customers?  matt
? 

How did you find your customers? 
Internal network 

How much can you make off this?  ben
[link market size question] - 4B / yr

How are you going to expand to more customers and a larger market?  ben
Beyond production planning for vehicle manufacturing, we’ve seen there is a larger need for demand estimation across (the entire economy) other consumer fields - hospitality, CPG, restauranting



What will the product look like in a few months?  mark
We hope to iterate with customers to really nail down the analysis and visualizations required to help them make planning decisions.
Part of this is making an AI generated feed that can let the users get to the point of whats happening on a day to day basis  
After that: we hope to lean into the idea of using LLMs and agents as a way for customers to interact with the data, to generate automated reports, and so on. 
In the long term we also plan to integrate user supply data so that we can automate the decisions themselves. 

What’s something you learned from customers?  matt
Industry specific stuff 

Are you planning to use customer data?  mark
Down the line we hope to integrate customer data.
By using supply data, we can get to the actual decision on what need to be produced. 

How are you going to make this sticky?  ben
The initial stickiness is that the problem we’re solving relies on having (roughly) real-time data to observe changes in consumer behavior.
Beyond that, we hope to upsell our customers on doing their production planning, which would be extremely sticky if we replace their in place assets.

Are you planning to do this for e-commerce?  mark
It’s possible but not on the roadmap 
