# 배열 비교하기

def solution(arr1, arr2):
    if(len(arr1) == len(arr2)):
      if(sum(arr1) > sum(arr2)): return 1
      elif(sum(arr1) < sum(arr2)): return -1
      else: return 0
    elif(len(arr1) > len(arr2)): return 1
    elif(len(arr1) < len(arr2)): return -1

print(solution([100, 17, 84, 1],[55, 12, 65, 36]))