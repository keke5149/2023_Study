#5639 트리
#왼쪽자식 < 부모 < 오른쪽 자식 / preorder 결과로 postorder 출력하기
#남의 풀이 이해도 어렵다...
import sys
sys.setrecursionlimit(10**6) #제한 안 해주면 런타임에러남
input = sys.stdin.readline
nodes = []
while 1: #입력값 개수 모름
    try:
        nodes.append(int(input()))
    except:
        break

def postorder(first, end): # 왼->오->루트
    if first > end: #인덱스 역전
        return
    else:
        mid = end + 1
        for i in range(first+1, end+1): #제일 왼쪽으로 이동(이전 값(first)보다 커질 때까지)
            if nodes[first] < nodes[i]: #현재(first)값보다 큼 == 오른쪽 서브트리 시작
                mid = i #mid: 트리 나뉘는 지점(루트)
                break
    postorder(first+1, mid-1) #first+i를 시작으로 트리확인(first의 왼쪽)
    postorder(mid, end) #오른쪽 서브트리 확인
    print(nodes[first])

postorder(0, len(nodes)-1)


