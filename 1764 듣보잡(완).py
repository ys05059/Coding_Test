import sys
n,m = map(int,sys.stdin.readline().split())
set1 = set([sys.stdin.readline().strip() for _ in range(n)])
set2 = set([sys.stdin.readline().strip() for _ in range(m)])
result = list(set1 & set2)
result.sort()
print(len(result))
print(*result,sep='\n')