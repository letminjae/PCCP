from collections import defaultdict

str = input()

answer = 0

dict = defaultdict(list)
dict[2] = ['A', 'B', 'C']
dict[3] = ['D', 'E', 'F']
dict[4] = ['G', 'H', 'I']
dict[5] = ['J', 'K', 'L']
dict[6] = ['M', 'N', 'O']
dict[7] = ['P', 'Q', 'R', 'S']
dict[8] = ['T', 'U', 'V']
dict[9] = ['W', 'X', 'Y', 'Z']

for s in str:
  for key, value in dict.items():
    if s in value:
      answer += key
      break

print(answer+len(str))