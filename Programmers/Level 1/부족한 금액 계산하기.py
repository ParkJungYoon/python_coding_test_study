def solution(price, money, count):
    total = sum([price * n for n in range(1,count+1)])
    
    if money-total < 0:
        return total-money
    return 0