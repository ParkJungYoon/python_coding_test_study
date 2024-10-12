'''
앞에서 빼는거 뒤에서 빼는거 경합
1. 빼서 종류가 줄어드는 방향으로 한 개 뺌
2. 만약에 양쪽에서 빼도 종류가 같으면 뺐을 때 맵에서 개수가 줄어드는거부터

n이 크니깐 종류가 몇갠지 계속 세는건 비효율적

1차) 시간 초과 : n이 20만임

2차) 오른쪽을 늘려나가면서 종류가 2이하도록 체크, 2 넘어가면 왼쪽을 +1씩 올려줌.

'''
from collections import defaultdict


n = int(input())
s = list(map(int, input().split()))
# count는 종류 
left, right, count = 0, 0, 0
fruit = defaultdict(int)
result = 0

while right < n:
    
    print(left, right, count)
    if count <= 2:
        if fruit[s[right]] == 0:
            count += 1
        if count <= 2:
            result = max(result, right - left + 1)
        fruit[s[right]] += 1
        right += 1
    else:
        fruit[s[left]] -= 1
        if fruit[s[left]] == 0:
            count -= 1
        left += 1

    
print(result)

'''
n = int(input())
s = list(map(int, input().split()))
left, right = 0, n-1
fruit = defaultdict(int)

for i in range(n):
    fruit[s[i]] += 1
count = len(fruit)
result = n

while True:
    if count <= 2:
        break
    result -= 1
    left_c = fruit[s[left]]
    right_c = fruit[s[right]]
    if left_c <= right_c:
        left_c -= 1
    else:
        right_c -= 1
    
    if left_c == 0 or right_c == 0:
            count -= 1

print(result)
'''