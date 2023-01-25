import sys
from collections import deque
from tabnanny import check
input = sys.stdin.readline

M,N,H = map(int,input().split())
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]

def check_graph():
    for k in range(H):
        for j in range(N):
            print(graph[k][j])
        print()

queue = deque()
graph = []
for k in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,input().rstrip().split())))
        for i in range(M):
            if temp[j][i] == 1:
                queue.append((i,j,k))
    graph.append(temp)
count = -1
while queue:
    count +=1
    for _ in range(len(queue)):
        x, y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                queue.append((nx,ny,nz))

for k in range(H):
    for j in graph[k]:
        if 0 in j:
            count = -1
            break
print(count)
