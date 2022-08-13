import sys, heapq

n = int(sys.stdin.readline())
h = []
result = []
for _ in range(n):
    v = int(sys.stdin.readline())
    if v == 0 and len(h) == 0:
        result.append(0)
    elif v == 0:
        result.append(heapq.heappop(h))
    else:
        heapq.heappush(h,v)
print(*result,sep='\n')


'''
h = []
for _ in range(n):
    value = int(sys.stdin.readline())
    if value: heapq.heappush(h, value)
    else: print(h and heapq.heappop(h) or 0)
'''