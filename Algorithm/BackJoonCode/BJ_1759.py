L, C = map(int, input().split()) #암호는 L자리
alphabet = list(input().split()) #len(alphabet) == C
alphabet.sort()
aeiou = ["a", "e", "i", "o", "u"]
password = []

def check(pw): #4개짜리 자모확인
    a, b = 0, 0
    for i in range(L):
        if pw[i] in aeiou:
            a += 1
        else:
            b += 1
    if a >= 1 and b >= 2:
        return True
    else:
        return False

def makePW(idx):
    if len(password) == L:
        if not check(password):
            return
        for i in password:
            print(i, end = "")
        print()
        return
        
    for i in range(idx, C):
        password.append(alphabet[i])
        makePW(i+1)
        password.pop()
makePW(0)
