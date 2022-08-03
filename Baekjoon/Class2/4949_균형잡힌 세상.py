from sys import stdin
input = stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break

    stack = []   
    answer = True
    for i in sentence:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if stack:
                check = stack.pop()
                if check != "[":
                    answer = False
                    break
            else:
                answer = False
                break
        elif i == ")":
            if stack:
                check = stack.pop()
                if check != "(":
                    answer = False
                    break
            else:
                answer = False
                break

    if not stack and answer:
        print('yes')
    else:
        print('no')