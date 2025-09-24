# 16953 - A->B

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
count = 1

while B != A:
    if B < A:
        count = -1
        break

    if str(B)[-1] == "1":
        B = int(str(B)[0:-1])
    elif B % 2 == 0:
        B = B // 2
    else:
        count = -1
        break
    
    count += 1

print(count)