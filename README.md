# IEEExtreme-Prime-Number
**Proposed problem in IEEExtreme 2016.**

This year I enjoyed **IEEExtreme** to see how the programming contest works, and for my surprise, it is **harder** than I thought it would be. :P

##The purpose

This problem was the last one (#25) of 2016 contest and it has a simple purpose:

* The user will enter with a number input in range (1, 10^18).
* The objectives are:
    * Verify if the number is prime.
    * If it is prime, return the number as a result of a sum of 3 prime numbers.
    * Ex: Input: 37       Output: 3 + 3 + 31 = 37.
    * Ex2: Input: 7283    Output: 7 + 23 + 7253 = 7283.

Having in mind that I can use whatever programming language to solve the problem, I chose Python because Python is wonderful. hehe </br>
I am **working to improve algorithm otimization**, but the main problem to identify and return the proposed number as a **sum of other 3 prime number is solved**.

##How it Works?

The main idea is verify if the number is **prime**, and if the result is positive, I search for the **last prime number** of input, using the same search way. </br>
In the moment that I find the last prime number of the input, I **calculate the difference between input** (if it is a prime number) **and its last prime number.** </br>

In almost all cases it will return me a short number, for example: 

Input: **3517** </br>
3517 is a prime number, so I calculate its last prime number, that is 3511. </br>
So, the difference is 3517 - 3511 = 6. </br>
Now, I only use the number 6. </br>
I verify **all the prime numbers between 2 and 6**. These numbers are: _[2,3,5]_. </br>
This way, I try a 3 terms sum with 3511 and all combinations in the difference list. </br>
In this case it will return the following result: **"3 + 3 + 3511 = 3517".** </br>
 
Here is the CodeSkulptor link for implementation:
http://www.codeskulptor.org/#user42_sAVxLToaP0_0.py

##Copyrigth

**The problem solution can be reproduced or shared in other medias**, but I only ask you to **maintain credits to author.** :) </br>
In addition, in case of **sharing CodeSkultpr code link**, please credit **Rice University** for platform development. 


Enjoy!

**Hollweg**


