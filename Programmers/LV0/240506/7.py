# 문자열 겹쳐쓰기

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

print(solution("Program29b8UYP","merS123",7))