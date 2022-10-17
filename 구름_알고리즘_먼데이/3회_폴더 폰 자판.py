# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
s = input()
dict = {1: ['1','.',',','?','!'], 2: ['2','A','B','C'], 3: ['3','D','E','F'], 4: ['4','G','H','I'], 5: ['5','J','K','L'], 6: ['6','M','N','O'], 7: ['7','P','Q','R', 'S'], 8: ['8','T','U','V'], 9: ['9','W','X','Y', 'Z']}

temp = s[0]
count = 0
answer = ''

for i in range(n):
	if temp == s[i]:
		count += 1
	else:
		length = count % len(dict[int(s[i-1])])
		answer += dict[int(s[i-1])][length-1]
		temp = s[i]
		count = 1
		
	if i == (n-1):
		length = count % len(dict[int(s[i])])
		answer += dict[int(s[i])][length-1]
	# print(answer)
		
print(answer)