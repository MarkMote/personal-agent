Intro
Describe what your company does in 50 characters or less.
Off-the-shelf perception software for robots 

What is your company going to make? Please describe your product and what it does or will do. 
We make software that helps robots see better. 

In order to know how to move, a robot must first understand its surroundings. A perception system is the set of sensors, hardware, and software that a robot uses to identify where it is, what’s around it, and how things are moving. Currently, obtaining perception is a major bottleneck in the development process, requiring a disproportionate amount of time and resources. This is mainly due to a lack of good off-the-shelf software solutions. Pythiea makes software to solve this problem.

Our solution uses camera feeds to generate a live map of a robot’s environment, including the locations of people, vehicles, and other objects of interest. A key feature of our software is its ability to interface with external (offboard) cameras. This has several advantages over conventional onboard-only perception, including: 
Greater reliability as external cameras can view from multiple visual perspectives, and can view things outside of a robot’s direct line-of-sight
Greater accuracy as fixed external cameras do not need to be localized (more than once). 
Lower cost as solving the problem externally uses less onboard compute and power, and a single offboard sensor can provide information to multiple robots.  



Robotics Specific Questions 
Where do you live now, and where would the company be based after YC? 
We are currently based in Midtown Atlanta. We’d be happy to move to get the most out of YC, but we aren’t sure where the company will be based after YC.

What is the “ex-factory” cost to make your device? How much do you charge/plan to charge per unit? 
N/A

Can you use off-the-shelf hardware instead of building custom? 
Yes - we don’t make our own camera hardware. Our software is very robust in terms of frame rate and resolution, so it works with just about any camera or camera network. 


Progress
How far along are you? 
Proof of concept tech development
Pilot with the city of Peachtree Corners, GA, where we are developing a large-scale prototype for automated driving applications. This is a smart city with continuous camera coverage over a ~1.5 mile stretch of road (https://www.curiositylabptc.com/startup-companies/)
Partnership with cloud provider (OVHcloud) 
Filing for a patent with a partnered law firm 
Currently talking with potential customers in robotics 

How long have each of you been working on this? How much of that has been full-time? Please explain. 
We began looking at the problem of robotic perception in August 2021. We started with the current camera-based approach in January 2022. Mark and Ben have been full time since December 2021. Matt has been full time since July 2022. 

If you are applying with the same idea as a previous batch, did anything change? If you applied with a different idea, why did you pivot and what did you learn from the last idea? 
We’re addressing the same problem, but now focusing on robotics companies rather than automotive manufacturers. We’re still very optimistic about helping self-driving cars as part of a long-term plan. However, we realized this would be a difficult space to break into initially because (i) OEMs are highly risk averse and have long acquisition cycles, and (ii) using public traffic cameras carries with it a certain amount of red tape. 

There are thousands of robotics companies that are currently suffering from this same core problem. They have an urgent need for this technology and have the ability to integrate new solutions immediately. 

If you have already participated or committed to participate in an incubator, "accelerator" or "pre-accelerator" program, please tell us about it. 
We participate in the (no commitment) Educate Program at ATDC (https://atdc.org/), a local state-funded organization, that provides mentoring and courses on customer discovery. We are also working with the (no commitment) ATDC 5G Connected Future Incubator. This is a community built around a smart city and autonomous vehicle testbed located in Georgia.



Idea 
Why did you pick this idea to work on? Do you have domain expertise in this area? How do you know people need what you're making? 
Reliable perception is the biggest barrier keeping robots from operating in the real-world. Robots tend to fail not from an inability to react to the things in their environment, but an inability to reliably make sense of their surroundings. If we can help solve this problem, we can help bring about the countless benefits of greater automation. 

We all met as graduate students at Georgia Tech while working in a robotics lab that specializes in safety for autonomous vehicles. Mark and Matt’s PhDs are on this topic. Ben worked at Yamaha after his Maasters, and his focus there was developing perception for self-driving boats. We have a collective 700+ citations in robotics literature and experience working on robotics projects at, to name a few: MIT, Stanford, Princeton, Dartmouth, NASA-JPL, AFRL, Raytheon, and General Atomics. Mark was also a developer for the Robotarium, an open-access multi-agent robotics research lab with hundreds of users around the globe. 

We know people need this because it is a problem that we experienced personally in our own projects. We also saw the problem arise repeatedly for others wherever we went. Perception is a universal pain point in robotics that is ripe for a better solution. 

Who are your competitors? What do you understand about your business that they don't? 
Optitrack and Vicon make external vision-based perception software and hardware, but their solutions require placing retroreflective markers on objects for localization and tracking. Stated another way, they build perception for lab environments, not the real-world.

Mobileye provides an onboard sensor suite for automotive applications with 11 cameras, per vehicle, plus additional sensors. Tangram Vision, Algolux, and SLAMCore design similar onboard perception solutions for robotics applications also utilizing a variety of sensors. 

We think that sharing information across vehicles and external sensors is currently a very undervalued approach. It adds technical complexity, but there's a lot of value if you can get it right. We understand that a perception solution must involve: 
better software, not just new hardware,
external cameras serving multiple robots, not multiple onboard sensors serving each robot, and
an ability to function in uncontrolled environments, not just the lab. 

How do you make money? How much could you make? 
We plan to offer a hosted version of our software with a tiered subscription model that scales with the number of cameras.

If we are able to provide the value of one additional perception engineer to 10 robotics companies, we will make on the order of $1M in revenue (our goal for 2023).

The total market for perception and related software is $30B, today, and will grow to $100B by 2030. At scale, if we are able to capture just 1% of that market, we would make $1B in revenue.







Legal 
Are any of the founders covered by noncompetes or intellectual property agreements that overlap with your project? If so, please explain.
No 

Who writes code, or does other technical work on your product? Was any of it done by a non-founder? Please explain. 
Everyone writes code and does technical work. Some code was written by a temporary employee, but all of the appropriate paperwork has been completed in terms of IP ownership. 

Have you received any government grants? If so, list the grants you've received, including the terms of the grant, who it's from, what it covers, and when you received it. 
We have not received any government grants. 

Is there anything else we should know about your company? 
No. 


Others 
If you had any other ideas you considered applying with, please list them. One may be something we've been waiting for. Often when we fund people it's to do something they list here and not in the main application.
1) Enter the AV market directly by building autonomous shuttles that utilize infrastructure. Shuttle routes could be entirely outfitted with external cameras to provide multiple layers of redundancy. 

2) Create an “app store” for robotics software. Currently there is a notable gap between free solutions (ROS, GitHub) and paid enterprise software. People selling their software (like us, along with some of the founders we know) need a place to be discovered and reviewed, and people purchasing the software need a trusted place to find it. Additionally, it would help to create a universal standard and significantly improve ease of integration.  

3) Simulink for robotics: a low-code robotics toolkit to help robotics companies bootstrap their development. Specifically, this would allow users to automatically generate (autocode) a base version of their software in a language such as C++ or Python from high-level specifications.  

Please tell us something surprising or amusing that one of you has discovered. 
It is entirely possible for animals to have wheels (https://arxiv.org/pdf/1909.11653.pdf).

You can use something called the “dirac belt trick” to produce unbounded rotation without a physical disconnect between wheel and axle. 


Curious 
What convinced you to apply to Y Combinator? Did someone encourage you to apply? 
We like the philosophy of YC and think it would help us scale faster. 

How did you hear about Y Combinator? 
Hacker News and startup lore


