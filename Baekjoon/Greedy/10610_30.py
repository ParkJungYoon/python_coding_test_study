n = input()
list_num = [i for i in n]

if sum(map(int,list_num)) % 3 != 0 or '0' not in list_num:
    print(-1)
else:
    list_num.sort(reverse=True)
    print(''.join(list_num))