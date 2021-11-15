def solution(l):
    counter = [0] * len(l)
    triples = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                counter[i] += 1
                triples += counter[j]
    return triples
