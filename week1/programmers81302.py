from collections import deque

def bfs(graph):
    visited = [[False]*5 for _ in range(5)]
    
    q = deque([])
    for ri in range(5):
        for li in range(5):
            if graph[ri][li] == 'P':
                q.append((ri, li))
    
    while q:
        x, y = q.pop()
        visited[x][y] = True
        first = graph[x][y] == 'P'
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if graph[nx][ny] == 'P':
                    return 0
                if graph[nx][ny] == 'O' and first:
                    q.append((nx, ny))
    return 1

        
def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer