import sys,math
input = sys.stdin.readline

t = int(input())

def func(m,n,x,y):
    # x는 index라 생각하면 편함
    while x <= m *n :                                # m,n의 최소공배수 구해서 넣어줘도 되지만 간단하게 m*n으로 구현
        if (x-y) % n == 0:                          # x의 배수 중에서 y의 배수 찾기
            return x
        x += m
    return -1

for _ in range(t):
    m,n,x,y = map(int,input().split())
    print(func(m,n,x,y))