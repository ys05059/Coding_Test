import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def bfs(tomato):
    stack = deque()
    for t in tomato:
        stack.append(t)
        visited[t[1]][t[0]] = 1
    while stack:
        v = stack.popleft()
        for x, y in [(v[0]+1,v[1]),(v[0],v[1]+1),(v[0]-1,v[1]),(v[0],v[1]-1)]:
            if 0<= x < M and 0 <=y < N and graph[y][x] == 0:
                if visited[y][x] == 0 or (0 < visited[y][x]and visited[y][x] > visited[v[1]][v[0]]+1):
                    stack.append((x,y))
                    visited[y][x] = visited[v[1]][v[0]] + 1
            
M,N = map(int,input().split())
graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]
tomato = []
for j in range(N):
    graph.append(list(map(int,input().rstrip().split())))
    for i in range(M):
        if graph[j][i] == 1:
            tomato.append((i,j))
        elif graph[j][i] == -1:
            visited[j][i] = -1

bfs(tomato)

result = 0
for j in range(N):
    if 0 in visited[j]:
        result = -1
        break
    result = max(result,max(visited[j])-1)

print(result)