def dfs(node, sheep, wolf, connect): #node에서 갈 수 있는 노드 리스트 connect
    global answer, case, mxsheep, tinfo
    if sheep == mxsheep:
        answer = sheep
        return
    
    if tinfo[node] == 0: #양이면
        sheep += 1
        answer = max(answer, sheep)
    else:
        if sheep > wolf + 1:
            wolf += 1
        else:
            return
    connect.extend(case[node])
    for c in connect:
        dfs(c, sheep, wolf, [i for i in connect if i != c]) #return돼서 올 때 sheep이나 wolf도 반영 안 되고 옴

def solution(info, edges):
    global answer, case, mxsheep, tinfo
    tinfo = info
    mxsheep = info.count(0)
    num = len(info)
    case = [[] for _ in range(num)]
    for e in edges:
        case[e[0]].append(e[1]) 
    answer = 0
    dfs(0, 0, 0, [])
    return answer

            
'''
def solution(info, edges):
    global answer
    visited = [0] * len(info)
    answer = 0
    def dfs(sheep, wolf):
        global answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return 
    
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0
    visited[0] = 1
    dfs(1, 0)
    return answer
'''