def solution(data, n):
    idcounts = {}
    filtered = []
    f = []
    for i in data:
        if i not in idcounts.keys():
            idcounts[i] = 1
        else:
            idcounts[i] += 1
    filtered = [a for a in data if idcounts[a] <= n]
    return filtered

print(solution([1,2,3],0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5],1))
