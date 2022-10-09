# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(A):
    # write your code in Python 3.6
    min_distance = abs(A[0]-A[1])
    for i in combinations(A,2):
        distance = abs(i[0]-i[1])
        if distance < min_distance:
            min_distance = distance
    
    if min_distance >= 100000000:
        return -1
    return min_distance
