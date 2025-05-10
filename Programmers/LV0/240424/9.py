# n번째 원소부터

# def solution(num_list, n):
#     return num_list[n-1:]

def solution(num_list, n):
    answer = []
    for i in range(n-1, len(num_list)):
      answer.append(num_list[i])
    return answer

print(solution([5, 2, 1, 7, 5],2))