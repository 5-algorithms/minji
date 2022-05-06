from dataclasses import dataclass
import sys
sys.stdin = open("sample.txt", "r")

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for k in range(i+1):
        dp = data[i][k]
        if k-1 >= 0:
            data[i][k] = max(data[i][k], dp + data[i-1][k-1])
        if k <= i-1:
            data[i][k] = max(data[i][k], dp + data[i-1][k])

print(max(data[n-1]))