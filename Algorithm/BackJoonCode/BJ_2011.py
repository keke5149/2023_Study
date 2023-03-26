#암호 해독, dp, 개수만 누적 합계
'''
25114
dp[1] = 1 // 2
dp[2] = 2 //2, 5 | 25
dp[3] = 2 //2, 5, 1 | 25, 1
dp[4] = 4 //2, 5, 1, 1 | 25, 1, 1 | 2, 5, 11 | 25, 11
dp[5] = //2, 5, 1, 1, 4 | 25, 1, 1, 4 | 2, 5, 11, 4|25, 11, 4|(n-1이랑) 2, 5, 1, 14|25, 1, 14|
'''
n = input()
length = len(n)
dp = [0 for _ in range(length+1)] # 길이 1 to n로 만들 수 있는 암호 개수
# 25114 -> dp[1] = 1; 2/ dp[2] = 2; 25, 2 5

if n[0] == '0': #0으로 시작하면 바로 컷
    print('0')
     
else:
    dp[0] = 1 #dp[i-2] 용    
    dp[1] = 1

    n = '0' + n #인덱스 맞추기용
    for i in range(2, length+1): 
        if n[i] > '0': #혼자서도 문자치환 가능 -> 이전 길이 암호(2511조합)에 n[i]문자(4) 하나만 추가되는 꼴
            dp[i] += dp[i-1] #디폴트 처리

        if n[i-1] != '0' and n[i-1] + n[i] <= '26': #두자리수로 봄 -> (251)조합에 n[i]+n[i+1] 문자(14) 하나만 추가
            dp[i] += dp[i-2]

    print(dp[length]%1000000)

'''
#걍 쌩으로... -> 안 되는 케이스 많음..
from string import ascii_lowercase
n = input()
length = len(n)
alphabet = list(ascii_lowercase)
pw= {}
for i in range(26):
    pw['i+1'] = alphabet[i]

string1 = []
answer = []
count = 0
def decoding(pi, si): #string1[si]에 넣을 거 찾기
    global string1, count, answer, n, length
    if pi < length:
        if n[pi] >= '3' or (pi+1) == length:
            string1.append(pw[n[pi]])
            decoding(pi+1, si+1)
        elif n[pi] != '0' and n[pi] + n[pi+1] <= '26':
            if n[pi] + n[pi+1] == '10' or n[pi] + n[pi+1] == '20':
                string1.append(pw[n[pi] + n[pi+1]])
                decoding(pi+2, si+1)
            else:
                string1.append(pw[n[pi]])
                decoding(pi+1, si+1)

                string1 = [string1[i] for i in range(si)] #리셋

                string1.append(pw[n[pi] + n[pi+1]])
                decoding(pi+2, si+1)
        else:
            print(0)
            exit(0)

    tmp = ''.join(string1)
    if tmp not in answer:
        answer.append(tmp)
        count += 1
decoding(0, 0)
print(count%1000000)
'''