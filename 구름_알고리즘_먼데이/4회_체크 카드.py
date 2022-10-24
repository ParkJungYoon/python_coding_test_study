# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import heapq
n, m = map(int,input().split())
# stack = []
heap = []

for i in range(m):
	command, num = input().split()
	if command == 'deposit':
		n += int(num)
	elif command == 'pay':
		if int(num) <= n:
			n -= int(num)
	elif command == 'reservation': 
		if heap or int(num) > n:	
			# stack.append(int(num))
			heapq.heappush(heap, int(num))
		else:
			n -= int(num)
	
	# if heapq:
	# 	for s in range(len(stack)):
	# 		if stack[s] <= n:
	# 			n -= stack[s]
	# 			del stack[s]
	# 			break
	
	if heap:
		# while heap[0] <= n:
		# 	n -= heapq.heappop(heap)
			
		if heap[0] <= n:
			n -= heap[0]
			heapq.heappop(heap)
print(n)