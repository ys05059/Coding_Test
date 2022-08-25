import sys
input = sys.stdin.readline

n = int(input())
graph = [ input().rstrip().replace(' ','') for i in range(n)] 

white = blue = 0

def divide_check(size,x,y):
    temp = '' 
    for j in range(size):
        temp += graph[y+j][x:x+size]
    
    return 0 if len(set(temp)) == 1 else 1

def dq(size,x,y):
    global blue 
    global white
    # 종료조건
    if size == 1 or not divide_check(size,x,y):
        if graph[y][x] == '1' :
            blue += 1
        else:
            white += 1
        return
    # 언제 나눌지
    ts = int(size/2)
    for dx, dy in [(x,y),(x+ts,y),(x,y+ts),(x+ts,y+ts)]:
        dq(ts,dx,dy)
dq(n,0,0)
print(white)
print(blue)