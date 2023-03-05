l, c = map(int, input().split())
str_arr = input().split()
str_arr.sort()

temp = []
consonants = []

def backtracking(start):
    if len(temp) == l and check(temp):
        print(''.join(temp))
        return
    
    for i in range(start, c):
        if str_arr[i] not in temp:
            temp.append(str_arr[i])
            backtracking(i+1)
            temp.pop()

def check(arr):
    vowel = 0
    consonants = 0
    for i in arr:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": 
            vowel += 1
        else:
            consonants += 1
    if vowel >= 1 and consonants >= 2: return True
    return False

backtracking(0)

'''
최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음 -> 이 조건을 깜빡함
'''