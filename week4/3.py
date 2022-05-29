# boj 3273
import sys
sys.stdin = open('sample.txt', 'r')

n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()
answer = 0
start, end = 0,n-1

while start < end:
    if data[start] + data[end] == x:
        answer += 1
        start += 1
    elif data[start]+data[end] > x:
        end -= 1
    else:
        start += 1

print(answer)
