import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    max_price = stock[-1]
    answer = 0
    for i in range(n-2,-1,-1):
        # 현재 가격이 더 싸면 구매해서 최대 금액으로 판다고 생각
        if stock[i] < max_price:
            answer += (max_price - stock[i])
        # 현재가 더 비싸면 max_price 갱신
        elif stock[i] > max_price:
            max_price = stock[i]
            # 최대일 때는 구매안하고 판매할거니깐 금액만 바꿔줘도 됨.

    print(answer)

'''
case 1
1
5
1 1 3 1 2

1
5
1 1 3 1 5
1) 구매 - 1
2) 구매 - 2
3) 구매 - 5
4) 구매 - 6
5) 판매 - 5*4 - 6 = 14

14?
'''
# 시간초과
# for _ in range(t):
#     n = int(input())
#     stock = list(map(int, input().split()))
#     cur_consum, cur_count = 0, 0
#     max_price = max(stock)
#     answer = 0
#     for i in range(n-1):
#         # 내일 오를거 같으면 주식 구매, 전체보다 크면 산다. 
#         if stock[i] < max(stock[i+1:]):
#             cur_consum += stock[i]
#             cur_count += 1
#         # 내일 떨어질거 같으면 일단 파는데, 현재 금액을 저장해뒀다가 더 큰 값이 나타나면 그때 파는걸로
#         elif stock[i] == max(stock[i:]):
#             answer += (stock[i]*cur_count) - cur_consum
#             cur_count = 0
#             cur_consum = 0
#     if cur_count != 0:
#         answer += (stock[-1]*cur_count) - cur_consum
#     print(answer)
        

# for _ in range(t):
#     n = int(input())
#     stock = list(map(int, input().split()))
#     cur_consum, cur_count = 0, 0
#     tmp_price, tmp_count = 0, 0
#     answer = 0
#     for i in range(n-1):
#         print(answer, cur_consum, cur_count)
#         # 이전에 팔았던거 재계산
#         if stock[i] > tmp_price:
#             answer += (stock[i]*tmp_count) - (tmp_price*tmp_count)
#         # 내일 오를거 같으면 주식 구매
#         if stock[i+1] >= stock[i]:
#             cur_consum += stock[i]
#             cur_count += 1
#         # 내일 떨어질거 같으면 일단 파는데, 현재 금액을 저장해뒀다가 더 큰 값이 나타나면 그때 파는걸로
#         elif stock[i+1] < stock[i]:
#             answer += (stock[i]*cur_count) - cur_consum
#             tmp_price = stock[i]
#             tmp_count = cur_count
#             cur_consum, cur_count = 0, 0
#     if stock[-1] > tmp_price:
#         answer += (stock[-1]*tmp_count) - (tmp_price*tmp_count)
#     if stock[-1] > stock[-2]:
#         answer += (stock[-1]*cur_count) - cur_consum
#     print(answer)
        
            

