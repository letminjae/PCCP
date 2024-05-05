# 배열 만들기 6

def solution(arr):
  stk = []
  idx = 0
  for i in range(len(arr)):
    if len(stk) == 0:
      stk.append(arr[idx])
      idx += 1
    elif len(stk) > 0 and stk[-1] == arr[idx]:
      stk.pop()
      idx += 1
    else:
      stk.append(arr[idx])
      idx += 1
  if len(stk) == 0: 
    return [-1]
  else: 
    return stk

print(solution([0, 1, 1, 1, 0]))