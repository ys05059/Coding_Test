import sys
import heapq

heap = []
l1 = []
result=[]
n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    for j in range(k):
        cal, val = sys.stdin.readline().split()
        if cal == 'I':
            heapq.heappush(heap,f[1])
        elif not heap:
            pass
        elif p == ('D',1) :
            heap = heapq.nlargest(len(heap))
            heapq.heapify(heap[1:])
        elif p == ('D',-1):
            heapq.heappop(heap)

    if not heap:
        result.append('EMPTY')
    else :
        heap = heapq.nlargest(len(heap))
        result.append("{} {}".format(heap[0],heap[-1]))

for s in result:
    print(s)



# 유성이 -> visited를 키로
