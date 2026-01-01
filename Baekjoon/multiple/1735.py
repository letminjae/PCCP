# 1735 분수 합

import math

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

numerator = (b*c + a*d) # 분자
denominator = b*d # 분모

gcd = math.gcd(numerator, denominator)

numerator = int(numerator / gcd)
denominator = int(denominator / gcd)

print(f'{numerator} {denominator}')