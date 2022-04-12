def solution(n):
    answer = [i for i in range(2,n) if (n-1)%i == 0]
    return answer[0]