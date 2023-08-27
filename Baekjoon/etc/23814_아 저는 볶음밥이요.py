d = int(input())
n, m, k = map(int, input().split())

remain_nm = sorted([d - n % d, d - m % d])
flag = False

if remain_nm[0] <= k % d:
    k -= remain_nm[0]
    flag = True

if remain_nm[1] <= k % d:
    k -= remain_nm[1]
    flag = True

if not flag:
    # 볶음밥 한 묶음 포기해서 n, m 나눠주는 경우는 만두 한 개 포기하고 두 개 받음 (총 1개 얻음)
    # 남는 볶음밥이랑 묶음 하나 더 추가
    temp_k = d + (k % d)
    if k >= temp_k and sum(remain_nm) <= temp_k:
        k -= sum(remain_nm)

print(k)

# d = int(input())
# n, m, k = map(int, input().split())

# def calculate_mandu():
#     return n // d + m // d + k // d

# check = calculate_mandu()
# max_mandu = calculate_mandu()
# max_rice = 0

# remain_n = d - n % d
# remain_m = d - m % d

# # n만 채워주기
# if remain_n >= k % d:
#     n += remain_n
#     k -= remain_n
#     if calculate_mandu() > max_mandu:
#         max_mandu = calculate_mandu()
#         max_rice = max(max_rice, k)
#     n -= remain_n
#     k += remain_n

# # m만 채워주기
# if remain_m >= k % d:
#     m += remain_m
#     k -= remain_m
#     if calculate_mandu() > max_mandu:
#         max_mandu = calculate_mandu()
#         max_rice = max(max_rice, k)
#     m -= remain_m
#     k += remain_m

# # n과 m 채워주기
# if remain_n + remain_m >= k % d:
#     m += remain_m
#     n += remain_n
#     k -= remain_m
#     k -= remain_n
#     if calculate_mandu() > max_mandu:
#         max_mandu = calculate_mandu()
#         max_rice = max(max_rice, k)
#     m -= remain_m
#     n -= remain_n
#     k += remain_m
#     k += remain_n

# if check >= max_mandu:
#     print(k)
# else:
#     print(max_rice)