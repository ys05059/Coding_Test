import sys
n,r,c = map(int, sys.stdin.readline().split())

result = 0
# 몇 사분면인지 체크하는 함수
def check(n,r,c):
    temp = pow(2,n-1)
    if r <= pow(2,n-1) and c <= pow(2,n-1):
        return 1
    elif r <= pow(2,n-1) and c > pow(2,n-1):
        return 2
    elif r > pow(2,n-1) and c <= pow(2,n-1):
        return 3 
    else :
        return 4

# 재귀함수
def recursive(n,r,c):
    global result
    if n == 0:
        print(result)
        return
    num = check(n,r,c)
    result += ((num-1) * pow(2,n-1)*pow(2,n-1))
    if num == 1:
        recursive(n-1,r,c)
    elif num == 2 :
        recursive(n-1,r,c-pow(2,n-1))
    elif num == 3 :
        recursive(n-1,r-pow(2,n-1),c)
    else :
        recursive(n-1,r-pow(2,n-1),c-pow(2,n-1))

recursive(n,r+1,c+1)