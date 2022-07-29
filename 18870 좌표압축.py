import sys
n = int (sys.stdin.readline())
l1 = list(map(int,sys.stdin.readline().split()))
l2 = sorted(list(set(l1)))

dic = {l2[i] : i for i in range(len(l2))}
for i in l1:
    print(dic[i],end = ' ')
