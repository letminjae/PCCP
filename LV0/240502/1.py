# 숨어있는 숫자의 덧셈 (2)

def solution(my_string):
  for v in my_string:
    if v.isalpha():
      my_string = my_string.replace(v, ' ')
  my_string = my_string.split()
  return sum(list(map(int, my_string)))