from collections import deque
from sys import stdin

def dfs (graph,v,visted):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs (graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v = map(int,stdin.readline().split())
'''그래프 구현'''
# 딕셔너리 초기화
adj = { key:[] for key in range(1,n+1)}
# edge 추가
for _ in range(m):
    src, dest = map(int,stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)
# 각 인접리스트 정렬
for key in adj.keys():
    adj[key].sort()

visited = [False] * (n+1)
dfs(adj,v,visited)
print()

visited = [False] * (n+1)
bfs(adj,v,visited)