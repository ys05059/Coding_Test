import sys
import copy
n = int(sys.stdin.readline().rstrip())

graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited1 = [ [0 for _ in range(n)] for _ in range(n)]

def dfs(x,y,visited):
    if visited[y][x]:
        return 0
    stack = [(x,y)]
    visited[y][x] = 1
    while stack:
        dx, dy= stack.pop()
        for a, b  in [(dx+1,dy),(dx,dy+1),(dx-1,dy),(dx,dy-1)]:
            if 0 <= a < n and 0 <= b < n and not visited[b][a]:
                if graph[b][a] == graph[dy][dx]:
                    visited[b][a] = 1
                    stack.append((a,b))
    return 1

count1 = count2 =0
for j in range(n):
    for i in range(n):
        count1 += dfs(i,j,visited1)
    graph[j] = graph[j].replace('G','R')

visited1 = [ [0 for _ in range(n)] for _ in range(n)]
for j in range(n):
    for i in range(n):
        count2 += dfs(i,j,visited1)

print(count1,count2)

# 더 나이스한 방법은 그냥 R에 G를 넣으면 되네;;