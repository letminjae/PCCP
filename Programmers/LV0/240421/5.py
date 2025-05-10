#배열의 유사도

def solution(s1, s2):
    answer = 0
    for i in s1:
      if i in s2: answer += 1
    return answer

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))