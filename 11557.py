num = int (input())
for i in range(num):
    snum = int (input())
    dic = {}
    for j in range(snum):
        tmp = input()
        print (tmp)
        key = tmp.split(0)
        val = tmp.split(1)
        dic[key] = val
    print(dic)
