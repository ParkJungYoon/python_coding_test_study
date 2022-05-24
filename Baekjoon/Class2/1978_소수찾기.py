n = int(input())
nums = map(int,input().split())

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num ** (1/2))+1):
        if num % i == 0:
            return False
    return True
result = len([i for i in nums if isPrime(i)])
print(result)