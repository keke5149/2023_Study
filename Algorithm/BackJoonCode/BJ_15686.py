from itertools import combinations
n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

house = []
chicken = []
for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            house.append([x, y])
        elif city[x][y] == 2:
            chicken.append([x,y])
        else:
            continue
        
#치킨집 m개 조합
chicken_m = list(combinations(chicken, m))

#치킨 거리 구하기
distance = []
for cm in chicken_m:
    chicken_t = cm
    distance_t = [] #한 조합에 대한 여러집의 치킨거리들
    for h in house:
        tmp = [] #한 집에서 갈 수 있는 치킨 집 m개에 대한 거리
        for c in chicken_t:
            tmp.append(abs(h[0]-c[0]) + abs(h[1]-c[1]))
        distance_t.append(min(tmp)) #한 집에서 갈 수 있는 치킨집 m 개 중 가장 가까운 거
        
    distance.append(sum(distance_t)) #치킨 집 조합 하나에서 나온 전체 치킨 거리

#결과
print(min(distance))