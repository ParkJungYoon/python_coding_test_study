import sys
input = sys.stdin.readline

t = int(input())

'''
서류 성적으로 1차 정렬을 한다.
그러면 일단 1번 인덱스는 무조건 뒤에 있는 애들보다는 하나라도 우수함.
앞에 지나온 인덱스의 2차보다만 높으면 됨.
'''

for _ in range(t):
    n = int(input())
    new_person = []
    for _ in range(n):
        primary, secondary = map(int, input().split())
        new_person.append((primary, secondary))
    
    new_person.sort()
    count = 1

    current_score = new_person[0][1]
    for i in range(1, n):
        if new_person[i][1] < current_score:
            count += 1
        
        current_score = min(current_score, new_person[i][1])
    print(count)