# 전년도 우승자가 후공
# 같은 점수(ex.7점)칸에 대해 더 많이 맞춘 사람이 점수(7점만)를 가져감 
# 같은 횟수를 맞췄으면 도전자가 점수를 가져감
# 둘 다 못/안 맞춤 -> 해당 점수는 아무도 못 가져감
# 최종 점수가 같을 경우 -> 도전자가 우승
# n = 5, info = [2,1,1,1,0,0,0,0,0,0,0]

# 조합(중복) 다 찾아서 하는 건 시간오래걸림
def solution(n, info):
    from itertools import combinations_with_replacement
    info.reverse()
    mx = -1
    answer = [-1]
    for comb in combinations_with_replacement(range(11), n):
        second = [0]*11
        for i in comb:
            second[i] += 1

        first, sec = 0, 0
        for i in range(11):
            if info[i] < second[i]:
                sec += i
            elif info[i] != 0:
                first += i

        if sec > first:
            if sec - first > mx:
                mx = sec - first
                answer = second
    return list(reversed(answer))

'''
#비트연산을 썼다는데 이해가 잘 안 됨.. 시간복잡도면에서 훨씬 낫다고...
def solution2(n, info):
    max = [-1] * 12
    for win in range(1 << 10):
        # 10 ~ 1의 점수별 화살 갯수, 0점 개수, 점수 차이
        cur = [0] * 10 + [n, 0]
        for i in range(10):
        	# 라이언 점수 획득
            if win & (1 << i):
                cur[-1] += 10 - i
                cur[-2] -= info[i] + 1
                cur[i] = info[i] + 1
            # 어피치 점수 획득
            elif info[i] != 0:
                cur[-1] -= 10 - i
                
        # 라이언이 지거나 화살을 n발 초과로 쏜 경우
        if cur[-1] <= 0 or cur[-2] < 0:
            continue
            
        # cur가 기존에 저장된 max보다 좋을 경우
        if cur[::-1] > max[::-1]:
            max = cur
    
    return [-1] if max[-1] <= 0 else max[:-1]
'''