# 2. 회원 할인
# 100 / 100

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        count = 0
        discount_ten = discount[i:i+10]
        for i in range(len(want)):
            if discount_ten.count(want[i]) == number[i]:
                count += 1
        if count == len(want):
            answer += 1

    return answer