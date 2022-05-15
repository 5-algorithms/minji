# 투포인터 연습하기
# boj2003

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
start = 0
end = 0

while start < n:
    s = sum(data[start:end+1])
    
    if s == m:
        count += 1
    
    if end == n-1:
        start += 1
        continue

    if s >= m:
        start += 1
    else:
        end += 1
    
print(count)