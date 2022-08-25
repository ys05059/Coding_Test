'''import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
output = []
for i in range(t):
    func = input().rstrip()
    n = int(input())
    if n < func.count('D'):
        output.append('error')
        input()
        continue
    l1 = deque(input().rstrip().replace("[","").replace("]","").split(','))
    # 언제 에러가 발생하는가 -> 배열길이가 D보다 적을 때

    reverse = 0
    for word in func:
        if word == 'R':
            reverse ^= 1
        else:
            if reverse :
                l1.pop()
            else:
                l1.popleft()

    if reverse:
        l1.reverse()
        output.append("["+','.join(l1)+"]")
    else :
        output.append("["+','.join(l1)+"]")

print(*output,sep='\n')
'''
for _ in range(int(input())):
    f=list(map(len,input().replace('RR','').split('R')))
    n=int(input())
    a=input()[1:-1].split(',')
    s,e=sum(f[0::2]),n-sum(f[1::2])
    a=a[s:e] if len(f)%2==1 else a[s:e][::-1]
    print(f"[{','.join(a)}]" if s<=e else "error")