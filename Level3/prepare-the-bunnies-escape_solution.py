def sp(map):
    h = len(map)
    w = len(map[0])
    visited = set()
    steps = 0
    tovisit = [(0, 0)]
    while tovisit:
        steps += 1
        for _ in range(len(tovisit)):
            i, j = tovisit.pop(0)
            if i == h - 1 and j == w - 1:
                return steps
            if (i, j) in visited:
                continue
            if map[i][j] == 0:
                visited.add((i, j))
                if i < h - 1:
                    tovisit.append([i+1, j])
                if j < w - 1:
                    tovisit.append([i, j+1])
                if i > 0:
                    tovisit.append([i-1, j])
                if j > 0:
                    tovisit.append([i, j-1])
    return 9999999
def solution(map):
    paths = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                map[i][j] = 0
                paths.append(sp(map))
                map[i][j] = 1
    return min(paths)

print(solution([[0]]))
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
