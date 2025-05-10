# 2525 오븐시계

hour, minute = map(int, input().split())
x = int(input())

hour += x // 60
minute += x % 60

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour, minute)