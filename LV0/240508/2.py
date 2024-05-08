# 문자열 밀기

def solution(A, B):
  if A == B:
    return 0
  for i in range(1, len(A)):
    A = A[-1]+A[0:-1]
    print(A)
    if A == B:
      return i
  return -1