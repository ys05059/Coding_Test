import sys
from collections import deque
from collections import defaultdict
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dic = defaultdict(list)
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0 for _ in range(n+1)]
def bfs(start):
    count = 0
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for k in dic[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = 1 
                count +=1
    return count

print(bfs(1))