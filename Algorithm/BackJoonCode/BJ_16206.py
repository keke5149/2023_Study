n, cut = map(int, input().split())
length = list(map(int, input().split()))
length.sort(key=lambda x: (x%10,x)) #작은 것부터 잘라야 최대 개수, x%10으로 해야됨 
count = 0
for cake in length:
        piece = cake//10
        if not cake%10:
            if piece-1 > cut:
                count += cut
                cut -= cut
            else:
                cut -= piece-1
                count += piece
        else:
            if piece > cut:
                count += cut
                cut -= cut
            else:
                cut -= piece
                count += piece
print(count)

#조건확인잘할것..(if문)