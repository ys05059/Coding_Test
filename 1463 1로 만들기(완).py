import sys
from collections import deque

n = int(sys.stdin.readline())
dist = [0 for _ in range(n+1)]

def bfs(start) :
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == 1:
            return dist[v]
        if v % 3 == 0:
            queue.append(int(v/3))
            if not dist[int(v/3)]:
                dist[int(v/3)] = dist[v] + 1
        if v % 2 == 0:
            queue.append(int(v/2))
            if not dist[int(v/2)]:
                dist[int(v/2)] = dist[v] + 1
        queue.append(v-1)
        if not dist[v-1]:
            dist[v-1] = dist[v] + 1

print(bfs(n))
         
        
'''
n = int(input())
arr = {1:0,2:1,3:1}

def find_num(num):
    if num == 1:
        return arr[num]
    elif num > 1: 
        if num in arr:
            return arr[num]
        else:
            if num % 6 == 0:
                temp = min(find_num(num//3), find_num(num//2))
            elif num % 3 == 0:
                temp = min(find_num(num//3), find_num(num-1))
            elif num % 2 == 0:
                temp = min(find_num(num//2), find_num(num-1))
            else:
                temp = find_num(num-1)
            arr[num] = temp + 1
            return arr[num]
answer = find_num(n)
print(answer)'''

'''
l={int(input())}
n=0
while 1 not in l:
	t=set()
    n+=1
	for i in l:
		if i%3==0:t.add(i//3)
		if i%2==0:t.add(i//2)
		t.add(i-1)
	l=t
print(n)
'''