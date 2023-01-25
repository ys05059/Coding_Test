import sys
input = sys.stdin.readline

def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3 :
        return 4
    else:
        return count(n-1) + count (n-2) + count(n-3)

t = int(input())
for _ in range(t):
    n = int(input())
    print(count(n))

