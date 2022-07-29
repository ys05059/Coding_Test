import sys

# 입력받기
n = int(sys.stdin.readline())
graph= []
for i in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

visited = [[0 for i in range(n)] for _ in range(n)]

def dfs (graph,i,j,dan):
    visited[i][j] = True
    count[dan] +=1
    for k in [(i,j-1),(i,j+1),(i+1,j),(i-1,j)] : 
       if 0<=k[0]<n and  0<=k[1]<n and graph[k[0]][k[1]] == 1:
            if not visited[k[0]][k[1]]: 
                dfs(graph,k[0],k[1], dan)

count = []
dan = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            count.append(0)
            dfs(graph,i,j,dan)
            dan += 1

print(dan)
count.sort()
print(*count,sep='\n')


