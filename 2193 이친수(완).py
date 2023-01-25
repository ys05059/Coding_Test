import sys
sys.setrecursionlimit(10000)
k = int(sys.stdin.readline())

a1 = 1
a2 = 1
temp = 0
for i in range(3,k):
    temp = a1 + a2
    a1 = a2
    a2 = temp
if k <= 2 :
    print(1)
else:
    print (a1 + a2)

'''
모범답안
a,b=1,1
for i in range(int(input())-2):a,b=b,a+b
print(b)
'''

def dp(n):
    if n == 1 or n==2:
        return 1
    return dp(n-2)+dp(n-1)
        