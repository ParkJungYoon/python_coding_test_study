n = int(input())

def prime_number(num):
    if num == 1: return False
    if num == 2: return True
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

# def palindrome(num):
#     num = str(num)
#     start, end = 0, len(num)-1
#     for _ in range(len(num)//2):
#         if num[start] != num[end]:
#             return False
#         else:
#             start += 1
#             end -= 1
#     return True

def palindrome(num):
    return str(num) == str(num)[::-1]

while True:
    check1 = prime_number(n)
    if check1:
        check2 = palindrome(n)
        if check2:
            print(n)
            break
    n += 1