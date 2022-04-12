def solution(n):
    n = int(n)
    nn = n ** (1/2)
    if nn%1 == 0:
        return (nn+1) ** 2
    else:
        return -1