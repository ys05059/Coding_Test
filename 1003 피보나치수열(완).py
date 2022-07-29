import sys
n  = int(sys.stdin.readline())
l1 = [0,0]
for _ in range(n):
    k = int(sys.stdin.readline())
    for t in range(k+1):
        if t == 0:
            l1 = [1,0]
        elif t == 1:
            l1 = [0,1]
            pre = [1,0]
        else:
            temp = l1
            l1 = [l1[0]+pre[0],l1[1]+pre[1]]
            pre = temp
    print(l1[0],l1[1])

