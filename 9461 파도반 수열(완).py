import sys
def pa(n):  
    a ,b, c  = 1, 1,1 
    for i in range (n-1):
        a ,b,c  = b, c, a+b 
    return a

t = int(input())
test = [int(sys.stdin.readline().strip()) for i in range (t)]

for i in test:
    print(pa(i))
    














# 재귀 풀이방법
# def pa(n):
#     if n in [1,2,3]:
#         return 1
#     else:
#         return pa(n-2)+ pa(n-3)

# t = int(input())
# test = [int(sys.stdin.readline().strip()) for i in range (t)]
# for i in test:
#     print(pa(i))