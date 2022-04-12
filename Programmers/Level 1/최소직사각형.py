def solution(sizes):
    a = max([max(i) for i in sizes])
    b = max([min(i) for i in sizes])
        
    return a * b