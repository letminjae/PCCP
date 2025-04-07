# 2753 - 윤년

N = int(input())

if N % 4 == 0:
    if N % 400 == 0 or not N % 100 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)