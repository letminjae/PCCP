# 5086 배수와 약수

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if a % b == a:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')