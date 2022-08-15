import sys
from unittest import result 
num = int(sys.stdin.readline())
graph = [[i for i in list(map(int,list(sys.stdin.readline().rstrip())))]for _ in range(num)]

def check(x,y,n):
    check =0
    for i in range(y,y + int(n/2)):
        check += sum(graph[i][x:x+int(n/2)])
    if check == 0 :
        return '0'
    if check == pow(int(n/2),2):
        return '1'
    else :
        return func(x,y,int(n/2))

def func(x,y,n):
    result =''
    if n == 1:
        return str(graph[y][x])
    #1사분면
    for dx,dy in [(x,y),(x+int(n/2),y),(x,y+int(n/2)),(x+int(n/2),y+int(n/2))]:
        result += check(dx,dy,n)
    if result.isnumeric():
        temp = sum(list(map(int,result)))
        if  temp == 0:
            return 0
        elif temp == 4:
            return 1
        else:
            return '('+result+')'    
    else : 
        return '('+result+')'
        

print(func(0,0,num))
# 무조건 네가지로 나누고 봐야함
# 시작과 끝에 괄호 넣어줘야함