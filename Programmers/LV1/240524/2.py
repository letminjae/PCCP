# 최대공약수와 최소공배수

def getGCD(a, b):
    if not b:
        return a
    else:
        return getGCD(b, a % b)
       
def solution(n, m):
    GCD = getGCD(n,m)
    LCM = n*m // GCD
    return [GCD, LCM]