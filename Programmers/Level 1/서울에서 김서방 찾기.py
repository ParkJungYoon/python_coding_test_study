def solution(seoul):
    for n in seoul:
        if n == "Kim":
            idx = seoul.index(n)
    answer = "김서방은 {0}에 있다".format(idx)
    return answer