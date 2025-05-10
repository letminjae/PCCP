#가장큰수찾기

# def solution(array):
#     answer = []
#     newarray = array.copy()
#     newarray.sort(reverse=True)
#     answer.append(newarray[0])
#     answer.append(array.index(newarray[0]))
#     return answer

def solution(array):
  answer = []
  answer.append(max(array))
  answer.append(array.index(answer[0]))
  return answer
    

print(solution([1, 8, 3]))

#max 함수를 알면 더쉽다