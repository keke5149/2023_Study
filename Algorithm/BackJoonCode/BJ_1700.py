n, k = map(int, input().split())
appliance = list(map(int, input().split()))

count = 0
plug = []

for i in range(k):
    if appliance[i] in plug:
        continue
    if len(plug) < n:#멀티탭 남은 거
        plug.append(appliance[i])
        continue

    #남은 자리가 없을 때
    index_list = []
    plugOX = 1
    for j in range(n):# 구멍개수만큼
        if plug[j] in appliance[i:]:
            index = appliance[i:].index(plug[j])
        else: #바로뽑아도됨
            index = 101 # 1<=k<=100
            plugOX = 0
        index_list.append(index)

        if plugOX == 0:
            break

    out_plug = index_list.index(max(index_list))
    del plug[out_plug]
    plug.append(appliance[i])
    count += 1
print(count)