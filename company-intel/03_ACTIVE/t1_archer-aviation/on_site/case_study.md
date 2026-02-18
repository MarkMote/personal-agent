# Flow

Work in: 
- Why safety? why its so important 
- safety in grad school 
- safety in pytheia 
- possible last slide: this is just a sliver, whats actually done was 
- Possible last slide: teasers for all the other projects, and what I've done since. 
    - one mutual connection with Marco
- IMPORTANT: overview of some of the work in gradschool 
- Important: 
    - Really good backup slides on anticipated questions 
- end: QR code with example: LOS controller implementation in safe cone 

Story point: 
- Introduce barrier functions 
- Talk about invariant sets 
    - the barrier function is just a statement: if you do this you will be safe
    - actual work is in this problem
- Compare:
    - gritsbots trial - mention robotarium
        - joke: is_invariant(set): return True
    - but thats not what we care about. We want systems like [list of examples we will go through]
        - double integator car
        - spacecraft rendezvous
        - spacecraft attitude control

- Ending recap: 
    - list out steps in safety filter design process
        - if invariant set is easy -> CBFs
        - else: find safety kernel and controller to it
    - same thing works for all the sysetms 
        - It works for a black box system! as long as you can
            (i) simulate 
            (ii) design a backup controller 
            (iii) find a safety kernel 
        - even better, you dont even have to prove invariance under the backup controller, you can just switch to any controller thats invariant in the backup set.


Need: 
- Find original presentation for thesis



## Slide 1: Covington GA (could be beginning or end)
Introduction:
So before getting into it, I'd like to say a few words on how my journey got started because I think it sets the tone for today. 
When I was looking into archer for the first time, I was interested to find that you don't make the planes here in CA, your manufacturing plant in a small town about an hour southeast of atlanta. 
Coincidentally, this is the town where I grew up, 
Its where in the summer before high school graduation, I worked as an electrician, and then I used that money to flip a car, so that I could afford the lessions over the next year. 

<!-- flying for the first time is  -->
<!-- But also i was actually terrified of heights, but could not resist the thrill of aviation. ' -->
Flight was both the most exciting, and most terrifying thing I've ever done. 
I'd like to make that theme central here today, because its been both the core of my work, and because I'd wager its the most important problem to archer as well.  
That is:
- how do you balance something as inherently complex and fast moving as flight, while 
- how do you build extremely complex fast moving in a way thats also extremely safe
- Or "Move Fast and **Not** Break Things" 

[image: map]
[image: plane]

work in: 
- Cessna 172 


## Slide 2: resume overview
Things I've done, how they relate to safety, and where this fits in
- one sentence on internships
- show point on timeline this relates to
- mention roostr and why I want to transition




## Slide: Safety Critical Control 
Pose the actual problem we are trying to solve 
xdot=f(x,u)

What it is, what its not 
What my focus is on: 
- applying this methodology to different systems 


## Invariant sets 




## Slide: RTA Approach 
Idea: decouple safety and control 


## Existing approaches and gaps 


## Slide: Robotarium 
mention in passing
How I got started. 
- straight forward implementation of 
software verification, monte carlo 


We did the not break things, but not the move fast 
Biggest problem I saw
- Invariant set was easy here - I mean it can just stop. 
- xdot = u. come on. 


