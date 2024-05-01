# 빈 배열에 추가, 삭제하기

def solution(arr, flag):
    X = []
    for i in range(len(flag)):
      if flag[i]:
        for j in range(arr[i]*2):
           X.append(arr[i])
      else:
        for j in range(arr[i]):
           X.pop()
    return X

print(solution([3, 2, 4, 1, 3],[True, False, True, False, False]))