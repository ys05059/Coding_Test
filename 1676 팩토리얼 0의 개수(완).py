import sys
n = int(sys.stdin.readline())
cnt = 0
for i in range(5,n+1,5):
    if i % 125 == 0:
        cnt +=3
    elif i % 25 == 0:
        cnt +=2
    else:
        cnt +=1
print(cnt)
