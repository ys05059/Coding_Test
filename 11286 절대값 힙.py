from select import select
import sys
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.items = [None]

    def check_small(self,a, b):
        if abs(a) < abs(b):
            return True
        elif abs(a)== abs(b) and a < b :
            return True
        else:
            return False

    def insert(self, value):
        l1 = self.items
        cur = len(l1)
        l1.append(value)
        while True:
            parent = cur // 2
            if cur >1 and self.check_small(l1[cur],l1[parent]):
                l1[cur], l1[parent] = l1[parent] , l1[cur]
                cur = parent
                continue
            break
        return

    def delete(self):
        l1 = self.items
        l1[1] , l1[-1] = l1[-1] , l1[1]
        min_value = l1.pop()
        last = len(l1) -1
        cur =1
        while True:
            left = cur*2
            right = cur*2+1        
            temp = cur
            if left <= last and  not self.check_small(l1[temp], l1[left]):
                temp = left
            if right <= last and  not self.check_small(l1[temp], l1[right]):
                temp = right
            if temp == cur:
                break 
            l1[temp], l1[cur] = l1[cur], l1[temp]
            cur = temp
        return min_value


n = int(input())
heap = MinHeap()
result = []
for _ in range(n):
    v = int(input())
    if v == 0 :
        if len(heap.items) == 1:
            result.append(0)
            continue
        else:
            result.append(heap.delete())
    else:
        heap.insert(v)

print(*result,sep='\n')