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
    
print(solution("5"))
print(solution("77"))
