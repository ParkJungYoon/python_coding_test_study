n, m = map(int,input().split())
p_list = []
pp_list = []
result = []
for i in range(m):
    p, pp = map(int,input().split())
    p_list.append(p)
    pp_list.append(pp)

if n%6 == 0:
    result.append(min(p_list)*(n//6))
    result.append(min(pp_list)*n)
else:
    result.append(min(p_list)*(n//6)+min(pp_list)*(n%6))
    result.append(min(pp_list)*n)
    result.append(min(p_list)*(n//6+1))

print(min(result))