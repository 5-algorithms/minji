# boj 2750
n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
for i in range(n):
    print(data[i])