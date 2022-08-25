import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

start = 0 
result = 0
unit = (2*n)+1
pn = 'IO'*n +'I'

def count_OI(line):
    count = 0 
    index = 0
    if line[0] == 'I':
        return count, index , False
    else:
        for i in range(1,len(line),2):
            if line[i-1] == 'O' and line[i] == 'I':
                count += 1 
                index += 2 
            elif line[i-1] == 'O' and line[i] == 'O':
                index += 2
                break
            else:
                break
        return count,index, True

out = 0

while start+unit < m:
    line = string[start:start+unit]
    if line[0] == 'O':
        start +=1 
        continue
    elif line == pn:
        count , index, check = count_OI(string[start+unit:])
        result += (1 + count)
        start += (unit+index)
    else:
        count = 0
        out = 0
        for i in range(1, unit):
            if line[i-1] == 'O' and line[i] == 'O': 
                count += 1
                out = 1 
            elif line[i-1] == 'I' and line[i] == 'I':
                count += 1
                out = 1
            elif line[i-1] == 'O' and line[i] == 'I':
                count += 1
            else : 
                if out :
                    break
                else :
                    count +=1
        start += count

print(result)


'''
모범 답안
n = int(input())
m = int(input())
expression = input()
answer = 0
i = 0
cnt = 0

while i < m-1:
    if expression[i : i+3] == 'IOI':
        i += 2
        cnt += 1

        if cnt == n:
            answer += 1
            cnt -= 1

    else:
        i += 1
        cnt = 0

print(answer)
'''