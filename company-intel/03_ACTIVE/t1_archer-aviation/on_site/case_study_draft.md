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
Dialogue:
So before getting into it, I'd like to say a few words on how my journey got started because I think it sets the tone for today. 
I was interested to find that archer does its manufacturing in a small town about an hour southeast of atlanta. 
Coincidentally, this is the town where I grew up, 

And if you could go back a few years there, you would seen the teenage me, who wanted to become a pilot,  working various jobs after school so that I could afford to take flight lessons in Covington Airport

The time I spent flying planes in Covington really instilled in me my love for aerospace. 
But I also remember being completely terrified at the same time, which ...

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
Dialogue: 
OK so sorry hitting you with a wall of text
I just want to quickly go through my background to help contextualize some of the content today. 
- Nearly everything I've done until my current job has related to safety in aerosace
    - was my thesis 
    - was most of my internships 
    - it was the entire point of my first startup 
- Today I'll mostly be touching on a few projects from grad school since i think they are most relevant. 


Things I've done, how they relate to safety, and where this fits in
- one sentence on internships
- show point on timeline this relates to
- mention roostr and why I want to transition
- reference: https://www.markmote.com/resume for a tight timeline


## Slide: Sections 
- Runtime assurance
    - introduce the 
    - about the tutorial paper I coauthored, which is really a nice intro
- Application to Spacecraft Proximity Operations 
    - work at AFRL on applying the theory to docking
- Application to Spacecraft Attitude Control 
    - another interesting application
- Planning for Failure 
    - ... 



## Slide: Safety Critical Control: Constraint Set 
Dialogue: 
Ok the next few slides are a bit dense, I'm assuming some familiarity with this, but just stop me if I skip over anything important
So first what do we mean by safety
Generally: it means freedom from harm, danger, damage, or failure of a mission 
The perspective we will take will be for control systems. 
... 
So for example CA tells you "no collisions" 
- it tells you what to do and not do
- but not how to do it or whether its even possible
- and there is no notion of time here
For that we need the notion of invariance 


## Safety Critical Control: Invariance and Safety 

Safety means satisfying contstraints for all time
More formally: We use the notion of forward invariance: meaning if you start in a set you will stay in that set 

A controller is safe if it renders the closed loop system forward invariant 
- footnote: link to formal definition in backup slide

Safety
If u:X->U renders the closed loop system forward invariant in CS subset CA
- u is a safe control law 
- CS is the safe set
- x\inCS is a safe state



## Control Invariance 
One more useful concept here: 
so far, weve focused on whether a control law is safe
But for design, iots useful to know: what sets can be made safe
- does such a control law even exist 

Control invariance: the set of states that **can** be rendered forward invariant 
- ie you can find a controller to make it safe
Viability Kernel: the largest control invariant subset
- ie its the best safe set we can hope to find 
Why do we care about large? because a large safe set means  that you are allowed to visit more states. 


## Visual Take: 
Sets we really care about
- State Space X 
- Allowable set of states CA 
- Safe Set 

Give examples


## RTA: Framework for solving safety 
Issue: only works for closed loop control policy
- controllers are complex 
- proving invariance gets harder with complexity
- and if you want to change the controler, you have to prove it again 
- and if you want a human to control you have no proofs 
RTA Idea: lets you solve the safety problem seperately, and override unsafe inputs 
- solves all of these problems 



How it works:
- Activate near the boundary of CS 

## Barrier functions: high level
Idea
- Find safe set CS = {x st h(x)>0} as a control invariant subset of CA
- solve QP: list equation 
- where Us: defined such that hdot(x,u) + alpha(h(x)) >= 0 
    - ie you are pulled back in the set near the boundardy 
- If CS is control invariant, the QP will always be feasible 


## Robotarium Example
- My first introduction to this was in the robotarium. 
- We used barrier functions to enable an open access lab. 
- Safety for gritsbot
- Dynamics
- Something actually unsatisfying to an aerosapce engineer about this. 
- Fails to capture somthing important 
    - most systems you cant just stop 

I have some backup slides on barrier functions, but the idea is just that ... 

And this is really the point where my research begins 

    - 

Include full details in backup slide'


## Online (Implicit) Methods
Key idea: 
but if you know of ANY invariant set, and can control there safely
You are in a control insariant set

So you you can replace:
- find CS 
With 
- Simulate online 

All you need is: 
- safety kernel, or backup set: Cb
- backup controller 

Worst case: follow the last safe trajectory



## Implicit Methods
- How do you actually find the Safe Set
- This is really what my research focused on 

Finding safe invariant sets is easy
But useful ones are large
and Large invariant sets are hard
but if you know of ANY invariant set, and can control there safely
You are in a control insariant set

So you dont actually need to know the safe set at all! 

## Implicit ASIF
- Coauthored this paper, mostly focusing on the applications 
- If you want the smooth filtering behavior you can get it anytime you can find sensitivity analysis on the outputs of a backup controller 

## Implicit Simplex
- interesting thing about this, you can take a trivial safe set
- very few assumptions on the system
    - no assumptions on the dynamics, relative degree, and so on

## Visual Take 2a

show both the approaches 

## Visual take 2b
Show the tradeoff 


## RTA: Summary 
I created this taxonomy
two dimentions for solving the problem 
- Online vs ofline 
- Switching vs non-switching

What makes it good: 
- minimize false positives 
- maximize 

## Next section: 
- Now we will get into the case studies. 
- Its about combingin this framework with engineering
- Applying it to real systems and the work that comes out of that 

## Arpod problem 
Take away from this section will be:
- MIPS approximate the viability kernel 



--- 

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


