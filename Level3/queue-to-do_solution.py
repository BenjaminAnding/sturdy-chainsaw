def solution(di, ci, tc):
    #your code here
    damage = 550
    crit = .05
    crits = (crit+ci)*tc
    return ((damage+di)*(tc-crits)+(((damage+di)*2)*crits))
casts = 100
base = solution(0,0, casts)
critincrease = solution(0,.01, casts)
dmgincrease = solution(5,0, casts)
print(base, critincrease, dmgincrease)
print(critincrease-base, dmgincrease-base)
