# 특이한 정렬

def solution(numlist, n):
  numlist = [(abs(n-num), -num) for num in numlist]
  numlist.sort()
  return [abs(num) for _, num in numlist]