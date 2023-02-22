n = int(input())
sign = list(input().split())
zeronine = [0]*10
minimum = ""
maximum = ""

def checkSign(i, j, k):# i: seq문자열 제일 마지막 숫자(문자), j: 이번에 테스트할 숫자(문자)
    if k == "<":
        return i<j
    else:
        return i>j

def makeString(length, fullstring):#문자열 길이 length: sign의 인덱스로도 씀
    global minimum, maximum

    if(length == n+1):
        if len(minimum) == 0:#mn에 지정된 거 없을 때(제일 처음. for로 돌리는 게 0부터 시작하니까 제일 처음이 제일 작다)
            minimum = fullstring
        else: #이후에 계속 갱신
            maximum = fullstring
        return

    for i in range(10):
        if zeronine[i] == 0:
            if length == 0 or checkSign(fullstring[-1], str(i), sign[length-1]):#빈 문자열이면 아무 숫자나 넣으면 되니까
                zeronine[i] = 1 #사용함
                makeString(length+1, fullstring+str(i))
                zeronine[i] = 0 #붙여서 문자열에 한번 썼다가 끝났으면 원상복구

makeString(0, "")
print(maximum)
print(minimum)