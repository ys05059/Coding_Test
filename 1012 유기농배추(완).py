import sys
test = int(sys.stdin.readline())
# def print_graph(graph,n,m):
#     for i in range(m):
#         for j in range(n):
#             print(graph[i][j],end= '')
#         print()
#     print()
def dfs(graph,x,y,n,m):
    stack = [(x,y)]
    while(stack):
        node = stack.pop()
        nx, ny = node[0],node[1]
        for tu in [(nx,ny+1),(nx,ny-1),(nx+1,ny),(nx-1,ny)]:
            if 0 <= tu[0] < n and 0 <= tu[1] < m and graph[tu[1]][tu[0]] == 1:
                stack.append(tu)
        graph[ny][nx] = 0
    return graph

result = []
for _ in range(test):
    cnt = 0
    n,m,k = map(int,sys.stdin.readline().split())
    # 그래프 초기화 및 그리기
    graph = [[0 for i in range(n)] for _ in range(m)]
    for i in range(k):
        dx, dy = map(int,sys.stdin.readline().split())
        graph[dy][dx] = 1
    
    #print_graph(graph,n,m)
    for j in range(m):
        for i in range(n):
            if graph[j][i] == 1:
                graph = dfs(graph,i,j,n,m)
                #print_graph(graph,n,m)
                cnt += 1
    result.append(cnt)
print(*result,sep='\n')