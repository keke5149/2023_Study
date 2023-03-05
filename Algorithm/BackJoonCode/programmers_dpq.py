from collections import deque
import heapq
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
def solution(operations):
    q = deque()
    for i in operations:
        j, k = i.split()
        k = int(k)
        print(k)
        if j == "I":
            q.append(k)
        elif j == "D" and q:
            if k == 1:
                q.remove(max(q))
            elif k == -1:
                q.remove(min(q))
        print(q)
    if q:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]
    return answer
print(solution(operations))

def solution2(operations):
    #힙 사용
    heap = []
    for i in operations:
        j, k = i.split()
        k = int(k)
        if j == "I":
            heapq.heappush(heap, k)
        else:
            if heap:
                if k == 1:
                    heap.remove(heapq.nlargest(1, heap)[0]) #heapq.nlargest(개수, iterable) 은 리스트를 반환
                else:
                    heapq.heappop(heap)
    if heap:
        answer = [heapq.nlargest(1, heap)[0], heap[0]]
    else:
        answer = [0, 0]
    return answer
print(solution2(operations))