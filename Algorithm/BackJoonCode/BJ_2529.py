n = int(input())
sign = list(input().split())
zeronine = [0]*10
minimum = ""
maximum = ""

def checkSign(i, j, k):
    if k == "<":
        return i<j
    else:
        return i>j

def makeString(length, fullstring):
    global minimum, maximum

    if(length == n+1):
        if len(minimum) == 0:
            minimum = fullstring
        else:
            maximum = fullstring
        return

    for i in range(10):
        if zeronine[i] == 0:
            if length == 0 or checkSign(fullstring[-1], str(i), sign[length-1]):
                zeronine[i] = 1
                makeString(length+1, fullstring+str(i)) #문자(숫자) i 붙여서 넘김
                zeronine[i] = 0

makeString(0, "")
print(maximum)
print(minimum)