#대문자와 소문자

def solution(my_string):
    answer = ''
    for str in my_string:
      if(ord(str) < 96): #대문자일때
         answer += str.lower()
      else: answer += str.upper()
    return answer

print(solution("aaaAAA"))

#isupper 를 사용하면 더 편했다