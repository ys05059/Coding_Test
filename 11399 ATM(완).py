import sys
n = int(sys.stdin.readline())
l1 = list(map(int,sys.stdin.readline().rstrip().split()))
l1.sort()
result = 0
for i in range(1,n+1):
    result += sum(l1[0:i])
print(result)