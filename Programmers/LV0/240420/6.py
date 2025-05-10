#문자열 정렬하기 (1)

def solution(my_string):
    answer = []
    for i in my_string:
      if(ord(i) < 97): answer.append(int(i))
    answer.sort()
    return answer

print(solution("abcd12392"))

# isdigit() 함수를 알았더라면....