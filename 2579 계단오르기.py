from sys import stdin
a,b,c = 0,0,0
n = int(stdin.readline())
for _ in range(n):
    pb = int(stdin.readline())
    a,b,c = max(b,c),a+pb,b+pb
print(max(b,c))

# 위 코드의 핵심 : n-1까지의 최댓값, n까지 올 수 있는 방법 2가지 저장하면서 앞으로 감

'''import sys
n = int(sys.stdin.readline())
v = [0]+[int(sys.stdin.readline().rstrip()) for _ in range(n)]

if n == 1:
    print(v[n])
else:
    f = [0]
    f.append((v[1],v[1]))
    f.append((v[2],v[1]+v[2]))
    for i in range(3,n+1):
        f.append((max(f[i-2][0],f[i-2][1])+v[i],f[i-1][0]+v[i]))
        #print("i:"+str(i)+" "+str(f[i]))
    print(max(f[n]))    
'''



'''
f[0] = 0
f[1] = [f[0]] + v[1]
f[2] = [f[0],f[1]] + v[2]
f[3] = [f[1],f[2]] + v[3]
f[4] = [f[2],f[3]] + v[4] # 이때는 f[3]의 리스트 중에 f[2]를 가지지 않는 것만
f[5] = [f[3],f[4]] + v[5] # f[3]을 통해서 받는건 max 때려도 되고 f[4]를 통해서 받는건 선택지 없음
'''