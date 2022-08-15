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

'''
from sys import stdin
input = stdin.readline


class Square:
    def __init__(self, x, y, size):
        self.x, self.y, self.size = x, y, size

    def _children(self):
        x,  y, m = self.x, self.y, self.size // 2
        return Square(x, y, m), Square(x, y+m, m), Square(x+m, y, m), Square(x+m, y+m, m)

    def encode(self):
        if self.size == 1:
            return IMAGE[self.x][self.y]

        code = ''.join(map(Square.encode, self._children()))
        return code[0] if code in ('1111', '0000') else f'({code})'


N = int(input())
IMAGE = [input() for _ in range(N)]
print(Square(0, 0, N).encode())
'''

'''
import sys

def main():
    N = int(sys.stdin.readline())
    board = []
    for _ in range(N):
        board.append(sys.stdin.readline())
    
    def check(row,col,l):
        if l==1:
            return board[row][col]
        else:
            half = l//2
            divide = [
                (0,0),(0,half),(half,0),(half,half)
            ]
            now = []
            for x,y in divide:
                now.append(check(row+x,col+y,half))
            l = 1
            for s in now:
                l *= len(s)
            if l==1 and now[0]==now[1]==now[2]==now[3]:
                return now[0]
            return "("+now[0]+now[1]+now[2]+now[3]+")"
    print(check(0,0,N))
main()
'''