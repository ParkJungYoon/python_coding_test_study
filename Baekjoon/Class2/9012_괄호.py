t = int(input())

for i in range(t):
    vps = input()
    stack = []
    answer = True
    for i in vps:
        if i  == "(":
            stack.append(i)
        else:
            if stack:
                check = stack.pop()
                if check != '(':
                    answer = False
            else:
                answer = False
    if answer and not stack:
        print('YES')
    else:
        print('NO')        
    