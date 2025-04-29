# 1259 팰린드롬수

while True:
    N = int(input())

    if N == 0:
        break

    if str(N) == str(N)[::-1]:
        print("yes")
    else:
        print("no")