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

'''
#조합으로 풀기
from itertools import combinations
import sys
l, c = map(int, input().split())
alphabet = list(sys.stdin.readline().split())
alphabet.sort()
comb = list(combinations(alphabet, l))
aeiou = ["a", "e", "i", "o", "u"]
def check(seq):
    a, b = 0, 0
    for i in seq:
        if i in aeiou:
            a += 1
        else:
            b += 1
    if a >= 1 and b >= 2:
        return True
    else:
        return False

for c in comb:
    if check(c):
        print(*c, sep="")
'''