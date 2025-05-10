# 분수의 덧셈

import math

def solution(ja1, mo1, ja2, mo2):
    boonmo = mo1 * mo2
    boonja = ja1 * mo2 + ja2 * mo1
    
    gcdvalue = math.gcd(boonmo, boonja)
    
    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcdvalue, boonmo / gcdvalue]
    return answer

print(solution(1,2,3,4))