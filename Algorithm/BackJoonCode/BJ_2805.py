n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = max(height)

while(start <= end):
    length = 0
    mid = (start + end)//2
    for i in height: #나무 길이가 mid보다 길 때 자르고 남은 길이(위쪽)
        if i > mid:
            length += i-mid
    if length >= m: #같을 때도(->출력은 end)
        start = mid + 1
    else:
        end = mid - 1
print(end)