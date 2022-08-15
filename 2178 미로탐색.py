'''import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph =[[int(s) for s in input().split()[0]] for _ in range(n)]
def bfs(start):
    count = 1
    queue = deque([start])
    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            for dx, dy  in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if dx == (m-1) and dy == (n-1):
                    return count +1 
                if 0<= dx < m and 0<= dy <n and graph[dy][dx] == 1:
                    queue.append((dx,dy))
                    graph[dy][dx] = 0 
        count +=1

print(bfs((0,0)))

'''
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for dx, dy  in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if 0<= dx < m and 0<= dy <n and graph[dy][dx] == 1:
                if dx == (m-1) and dy == (n-1):
                    return graph[j][i] +1 
                queue.append((dx,dy))
                graph[dy][dx] = graph[j][i] +1 

print(bfs((0,0)))

# 왜 시간이 줄어들지 않는거지? 왜 72ms가 아닌 104ms가 나오는거야
# 어디서 시간이 많이 드는지 알고 싶다
# 일단 deque 쓰는데 시간 걸림
# rstrip()이 조금더 빨라 .split()[0] 보다
# 결론 -> 시간에 의미두지말자
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
def bfs(start):
    queue = [start]
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    count = 1
    while True:
        temp = []
        for i,j in queue:
            graph[j][i] = 0
            for di , dj in dir:
                if 0<= i+di < m and 0<= j+dj <n and graph[j+dj][i+di]:
                    if i+di == (m-1) and j+dj == (n-1):
                        return count +1 
                    temp.append((i+di,j+dj))
                    graph[j+dj][i+di] = 0 
        queue = temp
        count +=1
print(bfs((0,0)))