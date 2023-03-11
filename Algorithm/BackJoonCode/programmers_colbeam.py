#프로그래머스 기둥과 보
#설치 -> 일단 추가한 후 그 결과를 check(answer)로 확인
#삭제 -> 일단 삭제 후 ...
#set()을 선언해서 처리하는 게 시간효율면에서 낫다고 함
def check(answer):
    for x, y, t in answer:
        if t == 0: #기둥
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else: return False
        elif t == 1: #보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x+1, y, 1] in answer and [x-1, y, 1] in answer):
                continue
            else: return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, t, c in build_frame:
        if c == 1: #설치
            answer.append([x, y, t])
            if not check(answer):
                answer.remove([x, y, t])
                
        else: #삭제
            answer.remove([x, y, t])
            if not check(answer):
                answer.append([x, y, t])
    answer.sort()
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))