# 다음 큰 숫자

def solution(n):
  for i in range(n+1, 1000000+1):
    if str(bin(n))[2:].count('1') == str(bin(i))[2:].count('1'):
      return i