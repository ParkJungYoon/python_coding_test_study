from collections import deque

def solution(priorities, location):
    queue = deque([])
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    # print(queue)
    result = []
    while queue:
        cur_size = len(queue)
        cur = queue.popleft()
        for i in queue:
            if i[0] > cur[0]:
                queue.append(cur)
                break
        # print(queue)
        if cur_size != len(queue):
            result.append(cur[1])
    # print(result)
    return result.index(location) + 1