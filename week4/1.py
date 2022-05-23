# boj 2230
n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()

start, end = 0, 1
answer = int(1e9*2+1)

while start <= end and end < n:
    diff = data[end] - data[start]
    if diff == m:
        answer = m
        break
    elif diff > m:
        answer = min(answer, diff)
        start += 1
    else:
        end += 1

print(answer)
