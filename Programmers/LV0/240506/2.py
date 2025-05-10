# PCCE 기출문제 4번 / 저축

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1

print(month)