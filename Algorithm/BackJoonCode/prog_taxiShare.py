#합승 택시
#dp, 다익스트라 알고리즘(heap을 쓰는 게 효율적), 하나의 정점에서 출발한 모든 최단 경로
import heapq
def solution(n, s, a, b, fares):
    answer = 100000000
    connect = [[] * (n+1) for _ in range(n+1)] #각 노드에 연결된 노드 체크
    for t1, t2, fee in fares:
        connect[t1].append([t2, fee])
        connect[t2].append([t1, fee])

    def dijkstra(s):
        heap = []
        cost = [100000000] * (n+1) #s에서 각 idx로 가는 비용 초기화
        heapq.heappush(heap, (0, s)) #시작 노드 푸쉬
        cost[s] = 0

        while heap:
            currentcost, current = heapq.heappop(heap)
            if cost[current] < currentcost: continue #갱신할 거x 이미 최소

            for node, fee in connect[current]: #current에 연결된 노드들
                tmp = currentcost + fee
                if tmp < cost[node]:
                    cost[node] = tmp
                    heapq.heappush(heap, (tmp, node))
        return cost
    
    arr = [[]] + [dijkstra(i) for i in range(1, n+1)] #모든 노드에 대해 시행//어떤 중간 노드를 거쳐가는 게 빠른지 알아야 하므로

    for i in range(1, n+1):
        answer = min(arr[s][i] + arr[i][a] + arr[i][b], answer)
    return answer

#플루이드와샬 알고리즘
#모든 정점 -> 모든 정점
def floydWarshall(n, s, a, b, fares):
    answer = 100000000
    #노드 사이의 cost 초기화
    graph =  [[100000000]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
    for n1, n2, cost in fares:
        graph[n1][n2] = cost
        graph[n2][n1] = cost

    for t in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][t] + graph[t][j], graph[i][j])
    
    for i in range(1, n+1):
        tmp = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(tmp, answer)
    return answer
    
print(floydWarshall(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))