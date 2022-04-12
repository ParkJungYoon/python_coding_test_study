def solution(arr):
    head = arr[0]
    answer = [head]
    for i in arr[1:]:
        if head != i:
            answer.append(i)
            head = i
    return answer