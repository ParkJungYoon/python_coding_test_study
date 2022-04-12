def solution(n, k):
    answer = ''
    count = 0
    while n:
        answer += str(n % k)
        n = n // k
    answer = answer[::-1]
    result = answer.split('0')   
    for i in result:
        if len(i) != 0:
            if isPrime(int(i)):
                count += 1

    return count

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n ** (1/2))+1):
        if n % i == 0:
            return False
    return True