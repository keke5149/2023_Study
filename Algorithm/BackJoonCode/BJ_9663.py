#N-Queen, 퀸 n개가 n x n 체스판에서 서로 공격 불가하게 놓는 방법 수
#행 하나당 퀸 1개
#pypy3 써야 통과, python3은 시간초과
n = int(input())
answer = 0
board = [0] * n #말을 놓는 것뿐이라 2차원 배열 대신 1차원 배열 사용// board[x좌표] = y좌표
def check(x): #새로 말을 놓을 위치 
    for i in range(x): #(0, 0)에서 x행까지 확인
        if board[x] == board[i] or abs(x-i) == abs(board[x]-board[i]): #대각선 차이: x좌표 차==y좌표 차
                return False
    return True

def solution(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n): #col 이동하면서 확인
            board[x] = i
            if check(x):
                solution(x+1)

solution(0)
print(answer)
    
