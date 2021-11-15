def Bfs(C, F, s, t):
        n = len(C)
        queue = []
        queue.append(s)
        global level
        level = n * [0]  
        level[s] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): 
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[t] > 0


def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp


def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)]
        flow = 0
        while(Bfs(C,F,s,t)):
            flow = flow + Dfs(C,F,s,200001)
        return flow
    
def solution(entrances, exits, path): #using Dinic's algorithm    
    C = []
    s = 0 
    t = (len(path)-len(entrances)-len(exits))+1
    if len(entrances) == 1:
        s_row = path[entrances[0]]
        C.append(s_row)
    else:
        s_row = [0] * len(path[0])
        for i in range(len(entrances)):
            for j in range(len(path[entrances[i]])):
                s_row[j] += path[entrances[i]][j]
        C.append(s_row)
        s_row = [200001] * len(path[0])
        C.append(s_row)
    for i in range(0, len(path)):
        if i not in entrances and i not in exits:
            row = path[i]
            C.append(row)
    if len(exits) == 1:
        t_row = path[exits[0]]
        C.append(t_row)
    else:
        t_row = [200001] * len(path[0])
        C.append(t_row)
        t_row = [0] * len(path[0])
        for i in range(len(exits)):
            for j in range(len(path[exits[i]])):
                t_row[j] += path[exits[i]][j]
        C.append(t_row)
    return MaxFlow(C,s,t)
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
