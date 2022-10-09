# 3. 짐 싣기
# 시간 초과

from collections import deque
# stack을 list로 구현하니깐 시간초과

def solution(order):
    answer = 0
    # main = deque([i+1 for i in range(len(order))]
    main = 1
    sub = []

    while True:
        if main == order[0]:
            main += 1
            order.pop(0)
            answer += 1
        elif sub:
            if sub[-1] == order[0]:
                sub.pop()
                order.pop(0)
                answer += 1
        else:
            sub.append(main)
            main += 1
        
        if main > len(order):
            if order[0] != sub[0]:
                break
    # while True:
    #     if main[0] == order[0]:
    #         main.popleft()
    #         order.pop(0)
    #         answer += 1
    #     elif sub:
    #         if sub[0] == order[0]:
    #             sub.popleft()
    #             order.pop(0)
    #             answer += 1
    #     else:
    #         box = main.popleft()
    #         sub.appendleft(box)
        
    #     if not main:
    #         if order[0] != sub[0]:
    #             break

    return answer

print('solution is', solution([4, 3, 1, 2, 5])) # 2
print('solution is', solution([5, 4, 3, 2, 1])) # 5
print('solution is', solution([5, 3, 4, 2, 1])) # 1
print('solution is', solution([2, 4, 5, 3, 1])) # 5