l = int(input())
word = input()
r = 31
m = 1234567891
sum = 0
for idx, i in enumerate(word):
    sum += (ord(i)-96)*(r**idx)

print(sum%m)