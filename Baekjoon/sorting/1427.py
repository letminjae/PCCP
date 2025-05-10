# 1427 소트 인사이드

number = list(input())

number.sort(key=lambda x: int(x), reverse=True)

print(int(''.join(number)))