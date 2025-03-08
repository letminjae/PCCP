# 문자열 압축

def solution(s):
  min_length = len(s)

  for i in range(1, len(s)//2+1):
    result = ""
    count = 1
    prev = s[0:i]

    for j in range(i, len(s), i):
      next_str = s[j:j+i]

      if prev == next_str:
        count += 1
      else:
        if count > 1:
          result += (str(count) + prev)
        else: # count == 1일 때
          result += prev
        prev = next_str
        count = 1

    if count > 1:
      result += (str(count) + prev)
    else: # count == 1일 때
      result += prev

    min_length = min(min_length, len(result))
  
  return min_length



solution("abcabcabcabcdededededede") # 14