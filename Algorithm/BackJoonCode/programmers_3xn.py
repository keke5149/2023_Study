#3*n 직사각형에 2*1 타일 빈틈없이 붙이기
n = int(input())
def solution(n): #가로 길이 n(짝수), 세로 3, 점화식 만들어짐
    
    #f(n) = f(n-2)*3 + f(n-4)*2 + f(n-6)*2 + ... + 2 //n이 짝수로만 나옴 + 그냥 규칙 찾으면 됨
    dp = [0]*(n+1)
    dp[2] = 3 #기본 가능 방법의 수
    if n % 2 != 0:
        return 0
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2]*3 + 2
        for j in range(i-4, -1, -2):
            dp[i] += dp[j]*2
    
    
    answer = dp[n] % 1000000007
    return answer
print(solution(n))