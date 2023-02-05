town, truck_max = map(int, input().split())
n = int(input())
box = [0]*n
for i in range(n):
    box[i] = list(map(int, input().split()))
box.sort(key=lambda x:x[1]) #먼저 도착하는 마을순.

count = 0
rest_space = [truck_max]*town #필드(truck_max)말고 리스트로 마을별 남은 공간(==트럭용량) 판단
for s, r, b in box:
    minimum = truck_max #초기화
    for i in range(s,r): #출발지와 배송지 직전 마을 사이에서 마을끼리 수용가능 트럭 용량 비교
        if minimum > rest_space[i-1]:
            minimum = rest_space[i-1]
    minimum = min(minimum, b) #마을이 받을 수 있는 택배 수량과 보내야하는 택배 수 중 작은 값 선택  
    for i in range(s,r):
        rest_space[i-1] -= minimum #마을당 남은 택배용량 갱신
    count += minimum

print(count)