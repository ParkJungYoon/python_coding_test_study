def solution(n, arr1, arr2):
    result = []
    
    for i in range(n):
        a = bin(arr1[i] | arr2[i])
        a = a[2:].zfill(n)
        a = a.replace("1","#").replace("0"," ")
        result.append(a)

    return result