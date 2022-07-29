import heapq, sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range (n)]
h = []
for i in data:
    if i == 0:
        print(0) if not h else print(-heapq.heappop(h))
    elif i>0:
        heapq.heappush(h,-i)
