import sys
n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dic ={-1 : 0 , 0:0, 1:0}

# 나눠야하는지 말아야하는지 확인하는 함수
def check(dx,dy,num):
    k = graph[dx][dy]
    for i in range(dx,dx+num):
        for j in range(dy,dy+num):
            if k != graph[i][j]:
                return 0
    return 1

def count(dx,dy,num):
    if num == 1 or check(dx,dy,num) == 1 :
        # 종류 확인해서 카운트만 올리면 됨
        dic[graph[dx][dy]] += 1
    else:
        # 9분할하고 count 재귀
        temp = int(num/3) 
        for i in range(dx,dx+num,temp):
            for j in range(dy,dy+num,temp):
                count(i,j,temp)
count(0,0,n)
print(*(dic.values()),sep='\n')