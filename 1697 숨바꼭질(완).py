import sys
from collections import deque
MAX = 100001

def bfs (start):
    queue = deque([start])
    while queue:
        v = queue.popleft()      
        if v == k:
            return dist[v]
        for i in [v-1, v+1, 2*v]:
            if 0 <= i < MAX and  dist[i] == 0 and i!=n:
                queue.append(i)
                dist[i] = dist[v] +1 


n,k = map(int,sys.stdin.readline().split())
dist = [0] *MAX
print(bfs(n))













# 그리디 문제 ㄴㄴ DP 문제
#import sys
# def next(now):
#     global time 
#     if now != n: 
#         time +=1
#     if now == k:
#         return 0
#     elif now == k-1 or now ==0:
#         next(now+1)
#     elif now == k+1:
#         next(now-1)
#     else :
#         if k-now > now *2:              # 무조건 2배 해야할 경우
#             next(now*2)
#         elif k-(now*2) <-1:
#             next(now-1)
#         elif k-(now*2) >1:
#             next(now+1)
#         else:
#             next(now*2)                # 근접했을 때 2배

# n,k = map(int,sys.stdin.readline().split())
# time = 0
# next(n)
# print(time)

# import sys
# n,k = map(int,sys.stdin.readline().split())
# time =0
# while n != k:
#     print(n)
#     if n == 0 or n == k-1:
#         n +=1
#     elif n == k+1:
#         n -=1
#     else:
#         if k-n > n*2:
#             n *=2
#         elif k-2*n < -1:
#             n -=1
#         elif k-2*n > 1:
#             n +=1
#         else:
#             n *=2
#     time +=1
# print(time)
