'''
해당 묶음에 알파벳이 있는지를 체크해야하는데, 딕셔너리 이런걸로는 비교하기 어렵다. 문자열을 숫자로 바꿔서 두 리스트가 같은지 비교
65~122
'''

import sys
input = sys.stdin.readline

w_length, g_length = map(int, input().split())
w = input().rstrip()
s = input().rstrip()
count_w = [0] * 58
temp_s = [0] * 58
count = 0

for ww in w:
    count_w[ord(ww)-65] += 1

print(count_w)

for start in range(0, g_length-w_length+1):
    if start == 0:
        for tt in s[start:w_length]:
            temp_s[ord(tt)-65] += 1
    else:
        temp_s[ord(s[start-1])-65] -= 1
        temp_s[ord(s[start+w_length-1])-65] += 1

    if count_w == temp_s:
        count += 1

print(count)


'''
dic1 = {'A': 0, 'b': 2}
dic2 = {'A': 0, 'b': 1}
dic3 = {'A': 0, 'b': 2}

print(dic1 == dic2)  # False
print(dic1 == dic3)  # True

# 딕셔너리 풀이

import sys
from collections import defaultdict
input = sys.stdin.readline

w_length, g_length = map(int, input().split())
w = input().rstrip()
s = input().rstrip()
count_w = defaultdict(int)
temp_s = defaultdict(int)
count = 0

for ww in w:
    count_w[ww] += 1

for start in range(0, g_length-w_length+1):
    if start == 0:
        for tt in s[start:w_length]:
            temp_s[tt] += 1
    else:
        temp_s[s[start-1]] -= 1
        if temp_s[s[start-1]] == 0:
            del temp_s[s[start-1]]
        temp_s[s[start+w_length-1]] += 1

    if count_w == temp_s:
        count += 1

print(count)
'''


'''
# 1차 시도 : 정렬 -> 시간 초과

w_length, g_length = map(int, input().split())
w = [i for i in input().rstrip()]
w.sort()
s = [i for i in input().rstrip()]
count = 0

if w == sorted(s[0:w_length]): flag = True
else: flag = False

for start in range(1, g_length-w_length+1):
    if not flag:
        temp = s[start:start+w_length]
        temp.sort()
        if temp == w:
            count += 1
            flag = True
    else:
        if s[start-1] == s[start+w_length-1]:
            count += 1
        else:
            flag = False

print(count)
'''