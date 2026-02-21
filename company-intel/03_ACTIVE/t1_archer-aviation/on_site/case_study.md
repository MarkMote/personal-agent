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
        - inverted pendulum 
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


---


## Overview 

Introduction and Problem (5 minutes)
- What is meant by safety?
    - dynamics of a control system
    - safety constraints
    - safe means safety constraints are never violated
- The constraint set contains unsafe states, need concept of control invariance 
    - inevitable violations 
- safe control problem: always choose safe `u`
    - too restrictive 
    - have too balance safety with performance 
- Runtime assurance: decoupling the safety problem 
    - Framework for solving the safety problem by building a "safety filter" 
    - MUST: guarantee forward invariance if starting in a safe region 
    - What makes it good: practical considerations
        - follow udes as much as you can 
        - allow as many useful states as you can
- Problem: 
    - Given
        - dynamical system 
        - safety constraints: CA (e.g. collision avoidance)
    - Find
        - RTA: (x, udes) -> usafe 
- Whats next
    - I'm going to walk you 

Taxonomy of RTA (tutorial paper + implicit ASIF) (10 minutes)
- 
- Start with Barrier functions: SOTA
- Issue finding large invariant sets is difficult 
- Personal Story: Robotarium and control barrier functions
    - Applied CBF based QPs to keep gritsbots safe 
    - Show: contraint set, and the control invariant set 
- Solved Problem? 
    - Far from it! 
    - CBFs approach gives you sufficient condition for safety and a nice way to filter
    - But it requires finding a control invariant set
    - Works for not breaking things but not on things that move fast 
    - There do exist approaches for finding control invariant sets, but its not
- Observation: if you can find a safe path to a safe set, you are safe
- Implicit ASIF: 
    - Coauthored this paper: my coauthor had the idea, i did the application 
    - segway
    - spacecraft angular velocity dynamics
- But theres an even simpler way
    - AutoGCAS
    - Let's formalize the approach
NOTE: implicit approaches were the focus

Whats next: Implicit RTA Applications 
- The engineering:  
    - what makes a good backup controller 
    - how do you find a good backup set
    - what if you have other considerations than how hard you interrupt 
- 

Case Study 1: (10 minutes)
- AFRL work: apply to real problem: natural motion trajectories
- MIPs approximate the viability kernel! 
    - complete, etc 
    - while slow, there are theoretical guarantees 
- Implicit ASIF also works 

Case Study 2: (5 minutes)
- Attitude control problem 
- Line of sight constraints 
- Whats the controller: ok 
    - Actually pretty simple, agressive point away controller 
- Whats the safe set 
    - point away
- But we can make it more robust: 
    - Complementary research: Can simulate reachable sets fast 
    - So we could extend safety to the reach set! 
- 

Case Study 3: (< 5 minutes)
- What do you do when collision is inevitable? '
- Can we plan for the worst case senario 
- Anything useful to be said here? 
- Idea: 
    - model collisions
    - minimize damage
    - always stay feasible 



--- 



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




- Expanding the Definition





## Slide: Safety Critical Control 

What do I Mean by Safety? 

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


