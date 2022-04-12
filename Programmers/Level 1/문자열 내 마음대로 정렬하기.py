def solution(strings, n):
    return sorted(sorted(strings), key=lambda y:y[n])