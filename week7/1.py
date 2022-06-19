import sys
from collections import deque
sys.stdin = open('sample.txt', 'r')

n, m = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

Q = deque([])
Q.append((0, 0))

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            Q.append((nx, ny))

print(graph[n-1][m-1])
