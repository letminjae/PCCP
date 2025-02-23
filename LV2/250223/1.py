# 땅따먹기

# 실패 코드
# def solution(land):
#     answer = 0
#     for i in range(len(land)):
#       print(land[i])
#       max_number = max(land[i])
#       answer += max_number
#       print("max: ", max_number)
#       for j in range(4):
#         print(land[i][j])
#         if land[i][j] == max_number:
#           if i != len(land)-1:
#             land[i+1][j] = 0
#       return answer

# DP 사용한 코드
def solution(land):
  for i in range(1, len(land)): # 첫번째 행은 그대로 사용하므로 1부터 시작
    for j in range(4):
      max_value = float('-inf')
      for k in range(4): # 이전 행의 모든 열을 탐색
        print(land[i][j], land[i][k])
        if k != j: # 현재열과 같은열이 아니라면
          max_value = max(max_value, land[i-1][k]) # 이전 행의 최대값을 찾는다.
      land[i][j] += max_value # 현재 행의 최대값을 더해준다.

  return max(land[-1]) # 마지막 행의 최대값을 반환



solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]) # 16