from collections import deque
import sys

sys.stdin = open('sample.txt', 'r')

n = int(input())
pairs = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(pairs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

connected = deque([1])
visited[1] = True
answer = 0

while connected:
    node = connected.pop()
    if not visited[node]:
        answer += 1
        visited[node] = True
    for x in graph[node]:
        if not visited[x]:
            connected.append(x)

print(answer)
