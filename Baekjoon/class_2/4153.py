# 4153 직각삼각형 (Class 2)

while True:
    lst = list(map(int, input().split()))

    if sum(lst) == 0:
        break

    lst.sort()

    if lst[2]**2 == lst[0]**2 + lst[1]**2:
        print("right")
    else:
        print("wrong")