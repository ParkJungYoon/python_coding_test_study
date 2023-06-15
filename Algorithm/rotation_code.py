'''
시계 방향으로 90도 회전
'''

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist[::-1])))

for i in mylist:	# 기존 리스트
    print(i)

print()

for i in new_list:	# 회전한 리스트
    print(i)

'''
반시계 방향으로 90도 회전
'''

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))[::-1]

for i in mylist:	# 기존 리스트
    print(i)

print()

for i in new_list:	# 회전한 리스트
    print(i)