import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dic = defaultdict(list)
    n = int(input())
    for i in range(n):
        item , cate = input().rstrip().split()
        dic[cate].append(item)
    result = 1

    for key in dic.keys():
        result *= (len(dic[key])+1)
    result -=1
    print(result)
