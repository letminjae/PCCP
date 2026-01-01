# 2675 문자열 반복

N = int(input())

for _ in range(N):
  number, string = input().split()
  number = int(number)
  for str in string:
    print(str * number, end="")
  print()