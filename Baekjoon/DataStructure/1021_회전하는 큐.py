from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

'''
34567812 길이 8이니깐

6의 위치는 6-3=3 : 앞에 3개를 빼야함 vs 뒤에 (8-(3+1)=4)
2의 위치는 2-3 : -1
7의 위치는 7-3=4
'''

cursor = 0
queue = deque(range(1,n+1))
answer = 0

for cursor in range(m):
    check = queue[0]
    idx = queue.index(a[cursor])

    if idx == 0:
        queue.popleft()
    elif idx > (len(queue)//2):
        for i in range(len(queue)-1-idx):
            queue.appendleft(queue.pop())
        answer += len(queue)-idx
        queue.pop()
    else:
        for i in range(idx):
            queue.append(queue.popleft())
        answer += idx
        queue.popleft()

print(answer)