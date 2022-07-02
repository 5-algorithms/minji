from collections import deque
import sys
sys.stdin = open('sample.txt', 'r')
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# connected = deque([])

# def bfs(start):
#     connected.append(start)
#     while connected:
#         node = connected.pop()
#         if not visited[node]:
#             visited[node] = True
#             for x in graph[node]:
#                 if not visited[x]:
#                     connected.append(x)

def DFS(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        # bfs(i)
        DFS(graph, i, visited)

print(answer)