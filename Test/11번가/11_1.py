# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    bulb = [False] * (len(A) + 1)
    count = 0
    for i in A:
        check = len([bulb[j] for j in range(1,i) if bulb[j]])
        if check == (i-1):
            count += 1 
            bulb[i] = True
        else:
            bulb[i] = True
    return count
