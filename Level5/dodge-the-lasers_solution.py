from decimal import Decimal, getcontext
from math import floor
getcontext().prec = 101 # set precision
sqrt2 = Decimal(2).sqrt() # calculate sqrt(2) to precision

def answer(n): # recursive function to calculate 
    total = int(n*(n+1)//2) # total will at least equal this sum ( 1 + 2 + 3 ... + n )
    if n <= 1: # if n sufficiently small we can just calculate remaining total iteratively
        for i in range(n):
            total += int(floor(((i+1)*(sqrt2-1))))
        return total # we can return the total
    factor = int(n*(sqrt2-1)) # this factor represents the remainder of the sum
    total += ((n*factor) - int((factor*(factor+1)/2)) - answer(factor)) # the sum ( 1 + 2 ... + n ) + ( n remainders - the sum from 1 to the floor of nsqrt(2) - the sum of the floors of sqrt(2) to  n*sqrt(2) ) will give the erroneous precision! 
    return total # return the erroneous calculation! 

def solution(str_n):
    n = int(str_n) # convert n to an int
    return str(answer(n)) 
    
# Awesome game! Thanks for letting me play. Some of my code is pretty awful as I challenged myself to complete each challenge in one session.
# I know for certain my answer to "escape pods" is erroneous. I was able to solve it properly after submitting (WHOOPS!) by adding dummy sources 
# and dummy sinks given multiple source multiple sink problems, I kinda hacked it together for my submission and was lucky it worked.
# I was often sleep deprived by the time I submitted, which explains the quality of the code, but also why I didn't think to comment my solutions properly. 
# Levels 1 and 2 were extremely easy and I was able to solve all the challenges within quickly without having to search too much. I actually found the challenges
# in Level 3 to be more difficult than the challenges in Level 4 on average (although "find the access codes" is way too tempting to cheat on given a Google search 
# for "lucky triples" gives an excellent algorithm on the first result courtesy of stack overflow.) 
# Many people have violated the spirit of the game by documenting their challenges and solutions on github, (which I am thankful for in the case of "bringing a gun to a guard fight"
# as I was stumped for quite a while trying to do matrix multiplications to generate reflections. I was able to improve someone else's solution [they had unneccessary if statements]
# that was incredibly helpful in seeing the problem in a new light.) and while I know that if this is read the recruiter/engineer reviewing my code will have to take my word for it: 
# I can honestly say that I did not submit any solution that I was unable to understand. 
# p.s. I bought and read a good bit of the SRE O'Reilly book (with the monitor lizard on the cover), what I read was great! I would have finished it, but I was working for a software startup
# in Boston at the time and unfortunately left it on an office bookshelf where it was forever lost when the company decided to move office locations :( 
# Once again, great challenge! I thoroughly enjoyed it, even though it was hectic to complete as I received the time I received the invitation coincided with my final exams.
# I still have one remaining invite code, (shared the other with a groupmate from my course on Operating Systems [still using nachos eww]) So after you guys have had a chance to review, I will
# be deleting this run to run through again and hopefully get some different challenges!

print(solution("5"))
print(solution("77"))
