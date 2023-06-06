'''
큐 사이즈 n
(학생번호, 추천 수, 들어온 순서)
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
total = int(input())
recommend = list(map(int, input().split()))
queue = deque([])

flag = False
for i in range(len(recommend)):
    if not queue:
        queue.append((recommend[i], 1, i))
        continue
    
    for _ in range(len(queue)):
        # 큐에 같은 학생이 있는지 확인, 있으면 +1
        num, count, idx = queue.popleft()
        if num == recommend[i]:
            flag = True
            queue.append((num,count+1,idx))
        else:
            queue.append((num,count,idx))
    # 같은 학생도 없었고, 큐에 자리가 있을 때
    if len(queue) < n and not flag:
        queue.append((recommend[i], 1, i))
    # 같은 학생도 없었고, 큐에 자리가 없을 때  
    elif len(queue) == n and not flag:
        out_student = sorted(list(queue), key = lambda x: (x[1], x[2]))[0]
        queue.remove(out_student)
        queue.append((recommend[i], 1, i))
    flag = False
    print(queue)

result = []
while queue:
    result.append(queue.popleft()[0])
result.sort()

print(*result)

'''
3
8
1 1 1 2 2 3 3 4
    
# Answer
1 3 4
'''