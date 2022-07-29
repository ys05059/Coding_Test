import sys
from collections import deque
sys.setrecursionlimit(10000)                            # 이거 안해줘서 헤맸음..

n,m =  map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited =[False] * (n+1)
result = 0

# 그래프 구현
for i in range(m):
    a, b =  map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs (graph,v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)

for j in range(1,n+1):
    if visited[j] == False: 
        dfs(graph, j)
        result +=1

print(result)


# from sys import stdin

# n,m =  map(int,stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# visited =[False] * (n+1)
# clear =[False] * (n+1)
# result = 0

# # 그래프 구현
# for i in range(m):
#     a, b =  map(int,stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)


# def dfs (graph,v):
#     visited[v] = True
#     cnt = 0
#     clear_check =0
#     global result
#     print(v, end= ' ')
#     for i in graph[v]:
#         if visited[i]:
#             cnt += 1
#         if not visited[i]:
#             dfs(graph, i)
#     #     if clear[i]:
#     #         clear_check += 1
#     # if cnt == len(graph[v]):
#     #     for k in graph[v]:
#     #         clear[k] = True
#     # if clear_check == len(graph[v]):
#     #     result +=1

# for j in range(1,n+1):
#     if visited[j] == True:
#         pass
#     else:
#         dfs(graph, j)
#         result +=1
# print("result:"+ str(result))