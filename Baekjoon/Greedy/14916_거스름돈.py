n = int(input())

count = 0

five = n // 5
count += five
n -= five * 5

if five == 0:
    if n % 2 == 1:
        print(-1)
    else:
        print(n//2)
else:
    if n == 0:
        print(count)
    else:
        if n % 2 == 0:
            count += n // 2
            print(count)
        else:
            count -= 1
            n += 5
            if n % 2 == 0:
                count += n // 2
                print(count)
            else:
                print(-1)


'''
# 다른 사람 풀이 오.. 뭔가 간단하게 잘 했군

loop = n // 5
result = -1
for i in range(loop + 1):
    bal = (n - (5 * (loop - i)))
    if bal % 2 == 0:
        result = (loop - i) + ((n - (5 * (loop - i))) // 2)
        break
print(result)
'''