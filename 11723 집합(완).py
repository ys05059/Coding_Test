import sys
n = int(sys.stdin.readline())
s= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(n):
    temp= sys.stdin.readline().split()
    if temp[0] == 'add':
        s[int(temp[1])] = 1
    elif temp[0] == 'remove':
        s[int(temp[1])] = 0
    elif temp[0] == 'check':
        sys.stdout.write('1\n' if s[int(temp[1])] else '0\n')
    elif temp[0] == 'toggle':
        s[int(temp[1])] ^= 1
    elif temp[0] == 'all':
        s= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    else:
        s= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]