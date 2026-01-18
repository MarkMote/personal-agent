Describe what your company does in 50 characters or less 
Shared Perception for Automated Driving 
What is your company going to make? 
We are building a service that will allow self-driving cars to take advantage of external sensors. 
A perception system is the set of sensors, hardware, and software that a car uses to identify what else is on the road, where it is, and how it is moving. Today, automotive manufacturers include redundant perception systems on cars to improve performance - we will provide the same functionality without the extra sensors and hardware. 
To do this, we will use traffic cameras and vehicle telemetry to gather the information needed. Then we will process this information and share the results via the cell network. 
How long have the founders known one another and how did you meet? Have any of the founders not met in person?
We met through our lab in grad school in early 2018. We have been discussing working together on a startup since late 2019. We have also been living together since January 2021. 
How far along are you? 
Technical - we’ve done some proof of concept work to test the latency of accuracy of traffic cameras, using the streams at https://511ga.org/.

Operational - we’ve gotten API access to 3500 traffic cameras in Georgia through GA 511, and are working to get access to 1500 more on the highways. 
Customer - we’ve interviewed OEMs and Tier 1 suppliers, and are in the process of finding a development partner. We’ve also spoken with DOTs outside Georgia and several robotics companies. 
How long have each of you been working on this? How much of that has been full-time? Please explain:
We have all been working since August 2021 on related ideas, but specifically on this idea since January 2022 (when we realized it was possible). Mark and Ben have been full time since December 2021. Matt will become full-time this spring. 
If you have already participated or committed to participate in an incubator, "accelerator" or "pre-accelerator" program, please tell us about it.
We participate in the Educate Program at ATDC (https://atdc.org/), a local state-funded organization, that provides mentoring and courses on customer discovery. We are also working with the ATDC 5G Connected Future Incubator. This is a community built around a smart city and autonomous vehicle testbed located in Georgia. The specific focus is on 5G-enabled connected vehicles and infrastructure. 

Why did you pick this idea to work on? Do you have domain expertise in this area? How do you know people need what you're making? 
1) It will do good for the world - Reliable perception is THE problem for automated driving. If we can help solvecrack it, we can help save millions of lives, reclaim billions of hours wasted in traffic, and slow down climate change. just to name a few.
2) It’s the next great company that no one is building - We think the biggest autonomy company won’t won’t build cars, it will build the intelligence that connects all of the cars. 
We all met as graduate students at Georgia Tech while working in a robotics lab that specializes in safety for autonomous vehicles. Mark and Matt’s PhDs are on this topic. Ben worked at Yamaha after his Masters, and his focus there was on development of lidar and camera based mapping for marine navigation. 
OEMs and Tier 1 suppliers need affordable perception - they can’t afford to add the sensors they need, so they can’t get the perception reliable enough to ship features. We know this from our talks with engineers there, as well as personal experience. At his last job, Ben’s team was only able to get simpler, perception-free features into the production process because of the high unit costs imposed by required sensors. 
What's new about what you're making? What substitutes do people resort to because it doesn't exist yet (or they don't know about it)?
It will be the first service leveraging external sensors and hardware to do perception for autonomous vehicles. 
Currently, companies improve performance by adding more sensors onto a vehicle. But adding more sensors is costly and improvements are incremental because: (1) there is only so many sensors you can afford to add and (2) with the new sensors placed next to the old ones, you are looking at the same things from the same angles, and so you are prone to many of the same errors. 
The current approach makes sense if you are developing in isolation, but on a crowded road, you may have Cars A, B and C (and so on) many vehicles all looking at the same things, and individually trying to figure out what they are looking at, all the while there are traffic cameras viewing the entire scene from above. Trying to solve the same problem over and over for each car with no one talking to anyone else is both unnecessary and highly limiting. 
Pytheia’s approach is to let cars and traffic cameras talk. That is, to work together to build a common reference model of the world. Instead of adding more sensors to your car, you get access to the resources of every other car and traffic camera in the network. This also solves problems that onboard sensors are fundamentally incapable of solving. For example, seeing things not in your field-of-view. 
Or, by analogy:
- Driving with a basic set of sensors is like using your two eyes.
- Competitors solve the problem by adding more onboard sensors, which is like getting help from your passengers.
- What we are proposing is like having the ability to see what every other person on the road is seeing in real time. 
Who are your competitors, and who might become competitors? Who do you fear most? 
Mobileye (most feared) offers full onboard perception suites for automated driving, although it isn’t perfect and the full system is pricey. They seem to have a similar approach to perception, selling the concept of redundancy for reliability (https://www.mobileye.com/true-redundancy/). 
HERE, TomTom, and Inrix all provide some static map information to cars on the road today. DeepMap (acquired by NVIDIA) makes HD maps for autonomous vehicles. None of these mapping services include dynamic objects, and so none are solving the same problem as us. However, these companies are threatening if they become competitors due to their existing distribution channels. 
What do you understand about your business that other companies in it just don't get? 
1)  All self-driving cars are fundamentally trying to understand the same world. You can solve the problem poorly for each vehicle on its own, or pull together resources to get a much better solution. Shared HD static mapping has been successful for this reason, and we think it could be done for real-time perception as well. 
2)  Mounted traffic cameras are highly undervalued. Whereas one car may need a dozen or so sensors, one traffic camera can cover dozens of cars. 
3)  External perception is technically feasible. The biggest concerns with external perception are latency and accuracy - we’ve done some proof-of-concept work that leads us to believe it’s technically feasible. 
4)  Affordability and ease of integration are key decision factors for consumer automobile features 
How do or will you make money? How much could you make?
(We realize you can't know precisely, but give your best estimate.)
We will make money by charging for usage of our service, and in the future may engage in a subscription based model. According to the McKinsey Center for Future Mobility, the market for ADAS sensors will be $25B in 2025. Our goal is to offer our service at 1/10th the price of equivalent sensors - which gives us an addressable market of $2.5B. 
How will you get users? If your idea is the type that faces a chicken-and-egg problem in the sense that it won't be attractive to users till it has a lot of users (e.g. a marketplace, a dating site, an ad network), how will you overcome that?
Our target customers are automotive OEMs and suppliers, so we’ll acquire customers through enterprise sales. 
To make the service attractive initially, we plan to gain an initial mass of coverage through existing traffic cameras. There are a lot of these cameras already, and a lot more are being built. For instance, in 2015 Vox found 4150 traffic cameras in the US (https://www.vox.com/a/red-light-speed-cameras), now there are more than that in Georgia alone. We are currently working with DOTs to get access. 
Are any of the founders covered by noncompetes or intellectual property agreements that overlap with your project? If so, please explain.
No 
Who writes code, or does other technical work on your product? Was any of it done by a non-founder? Please explain.
Mark, Matt, and Ben all write code. No code was written by a non-founder. 
Have you received any government grants? 
No but we have just applied for two. 
Is there anything else we should know about your company? (Pending lawsuits, co-founders who have left, etc.)
No. 
Please tell us something surprising or amusing that one of you has discovered. (The answer need not be related to your project.)
It is entirely possible for animals to have wheels (https://arxiv.org/pdf/1909.11653.pdf). 


