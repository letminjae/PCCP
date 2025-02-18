# 시간복잡도 초과 실패
# from itertools import combinations

# def solution(number, k):
#   answer = list(combinations(list(number), len(number)-k))
#   return ''.join(sorted(answer, reverse=True)[0])

def solution(number, k):
  stack = []
  for num in number:
    # while break 조건 : k > 0
    # 스택이 비어있지않고 num이 스택 마지막값보다 크면 스택pop
    while k > 0 and len(stack) != 0 and stack[-1] < num:
      print(True)
      stack.pop()
      k -= 1
    stack.append(num)
  # 12번 TC 반례 ("10000", 2) : k가 남는경우
  if k > 0:
    stack = stack[:-k]
    print(stack)
  return ''.join(stack)