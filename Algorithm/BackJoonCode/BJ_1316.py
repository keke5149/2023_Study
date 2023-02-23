import sys
n = int(input())
words = []
for i in range(n):
    words.append(sys.stdin.readline())
count = 0
def checker(word):
    letters = []
    for i in range(len(word)):
        if word[i] not in letters:
            letters.append(word[i])
        else:
            if word[i-1] == word[i]:
                continue
            else:
                return False
    return True
    
for word in words:
    if checker(word):
        count += 1
print(count)
