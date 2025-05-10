# 이진수 더하기

def solution(bin1, bin2):
  bin1 = int(bin1,2)
  bin2 = int(bin2,2)
  answer = bin(bin1 + bin2)
  return answer[2:]
