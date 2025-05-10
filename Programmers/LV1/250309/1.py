# 브론즈 3 - 그리디 대표 문제
n = int(input())

for _ in range(n):
  money = int(input())
  for i in [25, 10, 5, 1]:
    print(money//i, end=' ')
    money = money%i