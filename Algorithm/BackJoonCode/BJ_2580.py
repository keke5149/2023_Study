import sys
sudoku = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

empty = [] #빈칸 좌표만 넣기
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append([i, j])

def checkNumber(x, y, k): #x좌표, y좌표, 해당 좌표 숫자 k
    if k in sudoku[x]:#행
        return False

    for i in range(9):
        if k == sudoku[i][y]: #열
            return False

    nx = x//3 * 3 # 3*3 칸 용
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if k == sudoku[nx + i][ny + j]:
                return False

    return True #아무것도 중복되지 않음

def game(idx):
    if idx == len(empty): #빈칸 다 채움
        for i in range(9):
            print(*sudoku[i])
        exit(0) #다 채웠으면 함수 끝내기
    
    for i in range(1, 10): #1에서 9까지 넣어보기
        x = empty[idx][0]
        y = empty[idx][1]

        if checkNumber(x, y, i):
            sudoku[x][y] = i
            game(idx + 1)
            sudoku[x][y] = 0
game(0)

#python3으로 하면 시간 초관데 pypy3로 하면 통과(1780ms)