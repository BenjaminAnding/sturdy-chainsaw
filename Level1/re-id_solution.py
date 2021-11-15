import math
def solution(i):
    primestring = "2"
    for num in range(3,99999,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            primestring += str(num)
    idString = primestring[i:i+5]
    return idString
