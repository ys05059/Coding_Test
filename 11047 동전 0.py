import sys
input = sys.stdin.readline

n, v = map(int, input().split())
l1 =[int(input().rstrip()) for _ in range(n)]
count = 0
for i in range(n-1,-1,-1):
    count += int(v/l1[i])
    v = int(v%l1[i])
print(count)
