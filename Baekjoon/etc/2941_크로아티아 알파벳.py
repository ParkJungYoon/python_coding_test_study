alpha = input()
count = 0

dic = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
idx = 0

while True:
    if idx >= len(alpha):
        break
    
    count += 1

    if alpha[idx] == "d":
        if alpha[idx:idx+3] == "dz=":
            idx += 3
            continue
    
    if alpha[idx:idx+2] in dic:
        idx += 2
    else:
        idx += 1

print(count)