numeric_expression = input()
number = []
sign = ["+"]
answer = 0

temp = ""
for i in numeric_expression:
    if i == "-" or i == "+": 
        sign.append(i)
        number.append(int(temp))
        temp = ""
        continue
    temp += i
number.append(int(temp))

# 계산 시작

flag = False
for s in range(len(number)):
    if sign[s] == "+":
        if flag: answer -= number[s]
        else: 
            answer += number[s]
            flag = False
    elif sign[s] == "-":
        answer -= number[s]
        flag = True

print(answer)