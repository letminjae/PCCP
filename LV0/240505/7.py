# 조건 문자열

def solution(ineq, eq, n, m):
  if eq != "!":
    return int(eval(str(n)+ineq+eq+str(m)))
  else:
    return int(eval(str(n)+ineq+str(m)))

print(solution("<","=",20,50))