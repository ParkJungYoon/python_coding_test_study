name = input()
name_dict = {}

for i in name:
    if i not in name_dict.keys():
        name_dict[i] = 1
    else:
        name_dict[i] += 1

print(name_dict)

letters = []
for letter in name_dict:
    letters.append((letter, name_dict[letter]))
letters.sort()
print(letters)

left = ""
mid = ""
for letter in letters:
    if letter[1] % 2 == 1:
        mid += letter[0]
    left += letter[0]*(letter[1]//2)
    print(left)

count = [i for i in name_dict.values() if i%2==1]

if len(count) >= 2:
    print("I'm Sorry Hansoo")
else:
    right = left[::-1]
    print(left+mid+right)