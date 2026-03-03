so i think these two things planted to seed for me, and later inspired 
what my research would be in, which is all entered around this question of ...

-- 
ok so a quick look at my background 
- i did a phd 
- a bunch of internships 
- and then founded two companies 

the take away here is that most of the 
--- 

in terms of outline we have four parts

---

so if the talk is about 
So the first thing we need to do is lay down exactly what we mean by that 

In means a lot of different things, but in this talk we will take the perspective of safety for an input constrained dynamical system with full state

here the state captures relevant ...

and its convienient to specify what should and shouldnt happen based on inequalities 

note that Ca is just a specification on the state at a moment in time

--- 

So in order for a system to be safe, it not just means being in CS but staying there for all time. 

A couple things to note here are that: 
- only makes sense
- the constraint set Ca is generally not itself safe 

--- 

to extend the analysis beyond specific control policies its useful to define control invariance 

-- 

to recap we look at safety in terms of three sets
 

 ---

 The problem so far is that safety proofs are tied to a specific control law 

--- 

as an example, one of the SOTA ways of dong this is barier functions 

At a very high level the idea is 

--- 

A great example of why this is so useful is 

--- 

the first thing i learned trying to apply this research to more complex systems is that 
the hard part is 

--- 

so the most important fact to the methods that i will talk about today is that you actually dont need to find the safe set in advance to 

--- 

To make this a little bit more formal, we can define the safe backward image of a small safe set Cb as follows 

--- 

so lookng at a discrete approximation here, the simplest thing you can do is 

If you do this, there are suprisingly few assumptions on the system 

-- 

One downside to switching is that you dont get this nice gradual intervention behavior 

--- 
