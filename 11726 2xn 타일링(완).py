import sys
input = sys.stdin.readline

n = int(input())
result = 0
a = 0
b = 1
for i in range(n):
    result = a + b
    a = b 
    b = result

print (result%10007)