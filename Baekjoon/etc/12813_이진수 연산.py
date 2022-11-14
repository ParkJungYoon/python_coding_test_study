A = int(input(), 2)
B = int(input(), 2)

print(bin(2**100001) + bin(A & B)[2:])
print(bin(A | B)[2:])
print(bin(A ^ B)[2:])

max_num = 2 ** 100000

print(bin(max_num + ~A))
print(bin(max_num + ~B))