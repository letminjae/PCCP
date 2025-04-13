str = input()
str = str.lower()

dict = {}
for s in str:
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1

dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))

if len(dict) == 1:
    print(dict[0][0].upper())
else:
    if dict[0][1] == dict[1][1]:
        print("?")
    else:
        print(dict[0][0].upper())