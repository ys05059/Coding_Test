import sys

dic = {}
n,m = map(int, sys.stdin.readline().split())
for i in range(1,n+1):
    dic[sys.stdin.readline().strip()] = i
   
list1 = list(dic.keys())
for j in range(m):
    input = sys.stdin.readline().strip()
    if input.isdigit():
        print(list1[int(input)-1])
    else: 
        print(dic[input])

