# 꼬리 문자열

def solution(str_list, ex):
    answer = ''
    for str in str_list:
      if ex not in str: answer += str
    return answer

print(solution(["abc", "def", "ghi"],"ef"))