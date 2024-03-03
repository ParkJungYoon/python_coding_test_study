s = input()

temp = set()

for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        temp.add(s[j:j+i])
        
print(len(temp))