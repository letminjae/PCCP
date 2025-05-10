# 2884 알람시계

a, b = map(int, input().split()) # a = "1", b = "2"

sumMinutes = a*60 + b - 45

if sumMinutes < 0:
    print(f'23 {60 + sumMinutes}')
else:
    print(f'{sumMinutes // 60} {sumMinutes % 60}')