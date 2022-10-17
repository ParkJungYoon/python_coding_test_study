# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
user_input = list(map(int, input().split()))

score = {}

for i in user_input:
	if abs(i) not in score.keys():
		score[abs(i)] = i
	else:
		score[abs(i)] += i

answer = sum(score.values())
print(answer)