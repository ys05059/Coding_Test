import sys
from functools import reduce
input = sys.stdin.readline
n ,m = map(int,input().split())

list1 = list(map(int,input().rstrip().split()))

list2 =[0] *(n+1)
for i in range(n):
    list2[i+1] = list2[i]+list1[i]

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    print(list2[b]-list2[a-1])  