m = int(input())
s = set([])

for i in range(m):
    command = input()
    if command == 'all':
            s = set(range(1,21))
    elif command == 'empty':
        s = set([])
    else:
        command, number = command.split()
        if command == 'add':
            s.add(number)
        elif command == 'remove':
            if number in s:
                s.remove(number)
        elif command == 'check':
            print(1) if number in s else print(0)
        elif command == 'toggle':
            if number in s:
                s.remove(number)
            else:
                s.add(number)
