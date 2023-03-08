#5x5 숫자판, 5번 이동
#만들 수 있는 서로 다른 여섯 자리 수들의 개수, 갔던 칸 다시ㅇㅋ, 0 시작 ㅇㅋ
import sys
input = sys.stdin.readline
board = [list(input().split()) for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
def check(r, c, ch):
    if len(ch) == 6:
        if ch not in answer:
            answer.append(ch)
        return
    
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        if 0<= x < 5 and 0 <= y < 5:
            check(x, y, ch + board[x][y])


for i in range(5):
    for j in range(5):
        check(i, j, board[i][j])
print(len(answer))
