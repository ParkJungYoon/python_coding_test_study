def solution(topping):
    answer = -1
    binary_search(topping,0,len(topping)-1)

    return answer

def binary_search(data,start,end):
    cnt = 0
    mid = (start+end)//2
    if start > end:
        return end

    left_side = len(set(data[start:mid]))
    right_side = len(set(data[mid:end+1]))
    print(left_side, right_side)
    
    if right_side == left_side:
        cnt += 1
    if right_side >= left_side:
        binary_search(data,mid+1,end)
    else:
        binary_search(data,start,mid-1)
    return print(cnt)

# [1,2,4,3,2,1,1]

## 시도 2
def solution(topping):
    answer = -1
    mid = len(topping) // 2
    binary_search(topping,0,mid,len(topping)-1)

    return answer

def binary_search(data,start,mid,end):
    # cnt를 default로
    cnt = 0
    # start, end만 매개변수로
    # mid = (start+end) // 2
    if mid > end or mid < start:
        return print(cnt)
        
    left_side = len(set(data[start:mid]))
    right_side = len(set(data[mid:end+1]))
    print(left_side, right_side)
    
    if right_side == left_side:
        cnt += 1
    if right_side >= left_side:
        binary_search(data,start,mid+1,end)
    else:
        binary_search(data,start,mid-1,end)

# 역시나 거의 다 시간초과

# def solution(topping):
#     cnt = 0
#     mid = 1
#     while mid < len(topping):
#         left_side = len(set(topping[0:mid]))
#         right_side = len(set(topping[mid:]))
#         if right_side == left_side:
#             cnt += 1
#         mid += 1
#     return cnt