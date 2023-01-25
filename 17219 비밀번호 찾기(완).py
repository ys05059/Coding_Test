import sys
input = sys.stdin.readline

m,n = map(int,input().rstrip().split())
dic = {}
for _ in range(m):
    add , pw = input().split()
    dic[add] = pw
for _ in range(n):
    add = input().rstrip()
    print(dic[add])