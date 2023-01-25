from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

def D(n,cmd):
    cmd += "D"
    return ((2*n)%10000,cmd)

def S(n,cmd):
    cmd += "S"
    if n == 0:
        return (9999,cmd)
    return (n-1,cmd)

def L(n,cmd):
    return ((10*n+(n//1000))%10000,cmd+"L")

def R(n,cmd):
    return ((n//10+(n%10)*1000)%10000,cmd+"R")


def bfs(start,end):
    queue = deque([(start,"")])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for val in [D(v[0],v[1]),S(v[0],v[1]),L(v[0],v[1]),R(v[0],v[1])]:
            if val[0] == end:
                return val[1]
            elif visited[val[0]] == False:
                visited[val[0]] = True
                queue.append(val)


for _ in range(n):
    visited = [False for _ in range(10000)]
    start, end = map(int,input().split())
    print(bfs(start,end))
# D : 2배 S : -1 L : 왼쪽으로 shift R : 오른쪽으로 shift
'''전략
첫번째 자리부터 맞춘다 ㄴㄴ
자리수부터 맞춘다 ㄴㄴ 
언제 2배를 해야할까?
움직여서 나오는 수
1238
2381
3812
8123

1개의 값에 대해 2배 -> 다른 숫자조합

최단경로
그래프 탐색 bfs?
맞다

'''
'''
참고코드
import sys
from collections import deque
input = sys.stdin.readline


# 숫자 연산을 활용하여 DSLR 변환 결과값 구하기
# L, R의 경우에는 문자열 형태보다 숫자 연산으로
# 구하는게 시간복잡도 측면에서 이득
def cal(n):
    yield ("D", (n * 2) % 10000)
    yield ("S", (n + 9999) % 10000)
    yield ("L", (n*10)%10000 + (n*10//10000))
    yield ("R", (n+10000)//10 + (n%10)*1000 - 1000)


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    path = [""]*10001 # 최단경로 역추적 리스트
    
    q = deque()
    q.append(A)
    
    # 최단경로 원소 유무로 탐색 여부를 판단하므로
    # 출발 노드의 최단경로도 어떤 값으로 초기화해두기
    path[A] = "start"
    
    while q:
        n = q.popleft()
        if n == B:
            print(path[B][5:]) # start 빼고 출력
            break
        
        for cmd, res in cal(n):
            if path[res]:
                continue
            
            path[res] = path[n] + cmd
            q.append(res)
'''
