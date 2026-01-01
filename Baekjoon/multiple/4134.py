# 4134 다음 소수

N = int(input())

def check(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

for _ in range(N):
    number = int(input())
    while True:
        if number == 0 or number == 1:
            print(2)
            break
        if check(number):
            print(number)
            break
        else:
            number += 1