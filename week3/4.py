n, s = map(int, input().split())
data = list(map(int, input().split()))

start, end, cur = 0, 0, data[0]
answer = 100001

while True:
    if cur < s:
        end += 1
        if end == n:
            break
        cur += data[end]
        
    else:
        answer = min(answer, end-start+1)
        cur -= data[start]
        start += 1
        
if answer < 100001:
    print(answer)
else:
    print(0)