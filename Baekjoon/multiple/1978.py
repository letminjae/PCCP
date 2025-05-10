# 1978 소수찾기

N = int(input())
lst = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
for number in lst:
    if is_prime(number):
        count += 1

print(count)