from collections import defaultdict 

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

end = 0
num_dict = defaultdict(int)
result = 0

for start in range(n):
    while end < n:
        if numbers[end] in num_dict:
            num_dict[numbers[end]] += 1
        else:
            num_dict[numbers[end]] = 1

        if num_dict[numbers[end]] > k:
            num_dict[numbers[end]] -= 1
            break
        end += 1

    temp = end - start
    if temp > result: result = temp 
    num_dict[numbers[start]] -= 1

print(result)

'''
반례
21 1
1 2 3 4 5 6 6 7 8 9 10 11 13 15 63 34 34 33 33 22 1
output : 10
'''

'''
- 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미한다.
- 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다.
'''