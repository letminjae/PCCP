# 7785 회사에 있는 사람

N = int(input())

dict = dict()

for _ in range(N):
    name, commute = input().split()
    dict[name] = commute

sorted_dict = sorted(dict.items(), key=lambda item:item[0], reverse=True)

for key, value in sorted_dict:
    if value == "enter":
        print(key)