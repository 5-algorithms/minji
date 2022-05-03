n = int(input())
data = list(map(int, input().split()))

lo = 0
hi = n-1
answer = 0

while lo < hi:
    mid = (lo+hi)//2
    if data[mid] < mid: lo = mid+1
    elif data[mid] == mid:
        answer = mid
        break
    else: hi = mid

if answer: print(answer)
else: print(-1)