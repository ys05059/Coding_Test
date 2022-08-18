import sys
from collections import defaultdict
from collections import deque
n,m = map(int, sys.stdin.readline().split())

dic = defaultdict(list)
for _ in range(m):
    k, v = map(int,sys.stdin.readline().split())
    dic[k].append(v)
    dic[v].append(k)

def bfs(start, end):
    visited = [0 for _ in range(n+1)]
    queue = deque([start])
    visited[start] = 1
    level = 0
    while queue:
        for i in range(len(queue)):
            v = queue.popleft()
            for a in dic[v]:
                if not visited[a]:
                    if a == end :
                        return level +1
                    queue.append(a)
                    visited[a] = 1
        level += 1 

result=[0]
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if j != i:
            count += bfs(i,j)
    result.append(count)

print(result.index(min(result[1:])))