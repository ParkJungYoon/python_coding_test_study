'''
풀이 1 : 백트래킹
'''

import sys
k = int(input())
sign = list(input().split())

combi = []
max_num = str(0)
min_num = str(sys.maxsize)

def backtracking(start, end):
    global max_num, min_num

    if len(combi) == k + 1:
        temp = ''.join(combi)
        if int(temp) > int(max_num): max_num = temp
        if int(temp) < int(min_num): min_num = temp
        return

    for num in range(start, end):
        if str(num) not in combi:
            combi.append(str(num))
            if len(combi) == k+1:
                backtracking(0, 10)
            else:
                if sign[len(combi)-1] == "<":
                    backtracking(num+1, 10)
                elif sign[len(combi)-1] == ">":
                    backtracking(0, num)
            combi.pop()

backtracking(0,10)
print(max_num)
print(min_num)


'''
풀이 2 : 구현 (채정님)
'''
'''
k = int(input())
signList = input().split()

def getMaxValue(k, signList):
    result = [9]
    for i in range(k):
        if signList[i] == '>':
            for num in range(result[i]-1, -1, -1):
                if num in result:
                    continue
                else:
                    result.append(num)
                    break
        else:
            result.append(result[i])
            for j in range(i, -1, -1):
                if signList[j] == '>':
                    break
                result[j] -= 1
    print(''.join(map(str, result)))

def getMinValue(k, signList):
    result = [0]
    for i in range(k):
        if signList[i] == '<':
            for num in range(result[i]+1, k+1):
                if num in result:
                    continue
                else:
                    result.append(num)
                    break
        else:
            result.append(result[i])
            for j in range(i, -1, -1):
                if signList[j] == '<':
                    break
                result[j] += 1
    print(''.join(map(str, result)))
            
getMaxValue(k, signList)
getMinValue(k, signList)
'''