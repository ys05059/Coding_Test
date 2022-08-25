'''import sys
input = sys.stdin.readline
target = list(map(int,list(input().rstrip())))
m = int(input())
button= [0,1,2,3,4,5,6,7,8,9]
broke_list = []
if m !=0: 
    broke_list = list(map(int,input().rstrip().split()))
button = sorted(set(button) -set(broke_list))

def get_num(list1):  
    snum =0
    for i in range(len(list1)):
        snum += list1[i] * pow(10,len(list1)-(i+1))
    return snum

# 작은 수 중에 가장 큰 수
t = get_num(target)

if t == 100:
    print(0)
elif not button :
    print(abs(100-t))
elif button == [0]:
    print(min(abs(100-t),t+1))
else:
    slist = [0 for _ in range(len(target))]
    check = 0
    for i in range(len(target)):
        if check == 1:
            slist[i] =button[-1]
            continue
        if target[i] in button:
            slist[i] = target[i]
        else:
            out = 0
            for k in range(i,-1,-1):
                # i 보다 작은 index 다 돌려야함
                for j in range(len(button)-1,-1,-1):
                    if button[j] < target[k] :
                        slist[k] = button[j]
                        check = 1
                        out = 1
                        break
                if out : break
                if target[k] < button[0]:
                    if k > 0 :
                        # 둘째자리 부터는 앞자리 하나 내리고 최댓값 가져오기
                        slist[k-1] = 0
                        slist[k] = button[-1]
                    else:
                        # 첫째자리는 그냥 0 넣어서 젤 앞자리 없애기 
                        slist[k] = 0
                    check = 1
                    out = 1
                else:   
                    slist[k] = button[0]
            if out and k < i : 
                slist[i] = button[-1]
                
    blist = [0 for _ in range(len(target))]
    check = 0 # 최솟값으로 채우기
    append_check = 0
    for i in range(len(target)):
        if check == 1:
            blist[i] =button[0]
            continue
        if target[i] in button:
            blist[i] = target[i]
        else:
            out = 0
            for k in range(i,-1,-1):
                # i 보다 큰 index 다 돌려야함
                for j in range(len(button)):
                    if button[j] > target[k] :
                        blist[k] = button[j]
                        check = 1
                        out = 1
                        break
                if out : break
                else:
                    blist[k] = button[0]
            if not out :
                append_check =1 
                check = 1
    if append_check:
        if button[0] == 0:
            blist = [button[1]]+blist
        else:
            blist = [button[0]]+blist

    s = get_num(slist)
    b = get_num(blist)
    if 0 not in button and s == 0 :
        print(min(abs(t-b)+len(blist),abs(100-t)))
    elif 0 not in button:
        print(min(abs(t-s)+len(str(s)),abs(t-b)+len(blist),abs(100-t)))
    else:   
        print(min(abs(t-s)+len(str(s)),abs(t-b)+len(blist), abs(100-t),t+1))


'''
# 참고 코드
import sys # 입력 처리용
main_ch = 100  # 현재 채널
ch = input() # 이동할 채널
cnt = int(input()) # 고장난 버튼 개수
Move_ch = abs(100 - int(''.join(map(str, ch)))) # 채널 이동 횟수
def IsCh100(ch): # 채널이 100인지 확인
    if ch == '100':
        print(0)
        sys.exit(0) # 종료
# 고장난 버튼이 없어서 입력이 0일 때
if cnt == 0:
    #-> 그냥 채널 입력, 100채널과 근접하면 +-이동
    IsCh100(ch)
    if Move_ch < len(ch):
        print(Move_ch)
        sys.exit(0)
    else:
        print(len(ch))
        sys.exit(0)
  # 고장난 버튼 집합
nButton = set(sys.stdin.readline().split())
if cnt == 10: # 모든 버튼이 고장
# -> +-로만 채널 이동
    IsCh100(ch)
    print(Move_ch)
    sys.exit(0)
   # 입력한 채널이 100이면 즉시 종결
IsCh100(ch)
  #여기부터 일반적인 처리 과정 기록
Low_num = -1  # 가능한 작은 채널
High_num = 500001 # 가능한 최대 채널
Ch_num = int(''.join(map(str,ch))) # 이동할 채널 정수화
  # 입력 채널 번호에 해당하는 버튼이 정상일 때
if len(set(ch) & nButton)== 0:
    print(min(Move_ch, len(ch)))
    sys.exit(0)
     #이동할 채널보다 작은 번호에서 입력 횟수 구하기
ableN = Ch_num-1
while ableN > -1 :
    if len(set(str(ableN)) & nButton) > 0:
        ableN -= 1
    else:
        Low_num = len(str(ableN)) + (Ch_num - ableN)
        break
         #이동할 채널보다 큰 번호에서 입력 횟수 구하기
ableN = Ch_num+1
while ableN < 1000000:
    if len(set(str(ableN)) & nButton) > 0:
        ableN += 1
    else:
        High_num = len(str(ableN)) + (ableN - Ch_num)
        break
    #작은 번호에서 경우를 찾지 못했다면(-1) 비교 대상에서 제외함
if Low_num == -1:
    print(min(Move_ch, High_num))
else:
    print(min(Move_ch, High_num, Low_num))



'''
노가다
import sys
input = sys.stdin.readline
target = list(map(int,list(input().rstrip())))
m = int(input())
button= [0,1,2,3,4,5,6,7,8,9]
broke_list = []
if m !=0: 
    broke_list = list(map(int,input().rstrip().split()))
button = sorted(set(button) -set(broke_list))

# print("button: ")
# print(button)

def get_num(list1):  
    snum =0
    for i in range(len(list1)):
        snum += list1[i] * pow(10,len(list1)-(i+1))
    return snum

# 작은 수 중에 가장 큰 수
t = get_num(target)
# for i in range(len(target)):
#     t += target[i] * pow(10,len(target)-(i+1))

if t == 100:
    print(0)
elif not button :
    print(abs(100-t))
elif button == [0]:
    print(min(abs(100-t),t+1))
else:
    slist = [0 for _ in range(len(target))]
    check = 0
    for i in range(len(target)):
        if check == 1:
            slist[i] =button[-1]
            continue
        if target[i] in button:
            slist[i] = target[i]
        else:
            out = 0
            for k in range(i,-1,-1):
                # i 보다 작은 index 다 돌려야함
                for j in range(len(button)-1,-1,-1):
                    if button[j] < target[k] :
                        slist[k] = button[j]
                        check = 1
                        out = 1
                        break
                if out : break
                if target[k] < button[0]:
                    if k > 0 :
                        # 둘째자리 부터는 앞자리 하나 내리고 최댓값 가져오기
                        slist[k-1] = 0
                        slist[k] = button[-1]
                    else:
                        # 첫째자리는 그냥 0 넣어서 젤 앞자리 없애기 
                        slist[k] = 0
                    check = 1
                    out = 1
                else:   
                    slist[k] = button[0]
            if out and k < i : 
                slist[i] = button[-1]
                
    
    # print(get_num(slist)) 

    blist = [0 for _ in range(len(target))]
    check = 0 # 최솟값으로 채우기
    append_check = 0
    for i in range(len(target)):
        if check == 1:
            blist[i] =button[0]
            continue
        if target[i] in button:
            blist[i] = target[i]
        else:
            out = 0
            for k in range(i,-1,-1):
                # i 보다 큰 index 다 돌려야함
                for j in range(len(button)):
                    if button[j] > target[k] :
                        blist[k] = button[j]
                        check = 1
                        out = 1
                        break
                if out : break
                else:
                    blist[k] = button[0]
            # if out and  k<i : 
            #     blist[i] = button[0]
            #     break
            if not out :
                append_check =1 
                check = 1
    if append_check:
        if button[0] == 0:
            blist = [button[1]]+blist
        else:
            blist = [button[0]]+blist

            # for j in range(len(button)):
            #     if button[j] > target[i] :
            #         blist[i] = button[j]
            #         check = 1
            #         break

            # if check == 0 and i > 0 and target[i] == button[-1]:
            #     blist[i-1] += 1
            #     blist[i] = button[0]
            #     check = 1
    s = get_num(slist)
    # for i in range(len(slist)):
    #     s += slist[i] * pow(10,len(slist)-(i+1))
    b = get_num(blist)
    # for i in range(len(blist)):
    #     b += blist[i] * pow(10,len(blist)-(i+1))
    # print(slist)
    # print(blist)
    # print(s)
    # print(b) 
    if 0 not in button and s == 0 :
        print(min(abs(t-b)+len(blist),abs(100-t)))
    elif 0 not in button:
        print(min(abs(t-s)+len(str(s)),abs(t-b)+len(blist),abs(100-t)))
    else:   
        print(min(abs(t-s)+len(str(s)),abs(t-b)+len(blist), abs(100-t),t+1))
    # 큰 수 중에 가장 작은 수
    # 100 주변 값들 예외처리

'''