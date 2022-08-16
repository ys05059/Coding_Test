import sys
import heapq
n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    min_heap = []  
    max_heap = []
    result=[]
    visited_dic = {}
    for j in range(k):
        cal, val = sys.stdin.readline().rstrip().split()
        val = int(val)
        if cal == 'I':
            heapq.heappush(min_heap,(val,j))
            heapq.heappush(max_heap,(-val,j))
            visited_dic[j] = 1
        elif (cal,val) == ('D',-1) :
            for _ in range(len(min_heap)):
                temp = heapq.heappop(min_heap)
                if visited_dic[temp[1]] == 1:
                    visited_dic[temp[1]] = 0
                    break

        elif (cal,val) == ('D',1):
            for _ in range(len(max_heap)):
                temp = heapq.heappop(max_heap)
                if visited_dic[temp[1]] == 1:
                    visited_dic[temp[1]] = 0
                    break

    check = False
    for _ in range(len(max_heap)):
            temp = heapq.heappop(max_heap)
            if visited_dic[temp[1]] == 1:
                check = True
                break
    if not check :
        print("EMPTY")
    else:
        result.append(-temp[0])
        for _ in range(len(min_heap)):
                temp = heapq.heappop(min_heap)
                if visited_dic[temp[1]] == 1:
                    visited_dic[temp[1]] = 0
                    break
        result.append(temp[0])
        print(*result,sep=' ')


# 왜 런타임 에러 (UnboundLocalError) 이 에러가 뜨는거지 전역변수 설정도 해줬는데
