#불량 사용자
#permutation 사용 -> banned_id 개수의 모든 조합 찾아두고 체크
from itertools import permutations

def check(user, banned):
    if len(user) != len(banned): return False
    else:
        for u, b in zip(user, banned):
            if b == '*': continue #먼저 확인
            if u != b: return False
        return True

def solution(user_id,banned_id):
    answer = []

    for usergroup in permutations(user_id, len(banned_id)):
        count = 0
        for u, b in zip(usergroup, banned_id):
            if check(u, b):
                count += 1
        if count == len(banned_id):
            if set(usergroup) not in answer:
                answer.append(set(usergroup))
    return len(answer)

'''
#불량 사용자에 모양이 같은 게 여러 개인 경우//*rodo(frodo), *rodo(crodo) 처리 못함
def solution(user_id, banned_id):
    dic = {}
    for idx, ban in zip(range(len(banned_id)), banned_id):
        dic[ban] = idx
    answer = []
    usr = []
    count = [0] * len(banned_id)
    for user in user_id:
        for banned in banned_id:
            print(banned, user)
            if len(user) != len(banned):
                continue
            flag = 0
            for i in range(len(banned)):
                if user[i] != banned[i] and banned[i] != '*':
                    flag = 1
                    break
            if flag == 0 and user not in usr:
                print("일치")
                usr.append(user)
                answer.append([banned, user])
                count[dic[banned]] += 1
    ans = 1
    print(count)

    #*처리된 모양이 똑같은 경우...

    for i in count:
        if i == 0: continue
        else: ans *= i
    print(ans)
    return answer
'''
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
