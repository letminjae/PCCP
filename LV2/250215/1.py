# 메뉴 리뉴얼

from itertools import combinations

def solution(orders, course):
  answer = []

  # 몇개의 요리로 구성? 2, 3, 4
  for count in course:
    count_dict = {}

    # 주문에서 단품메뉴 쪼개서 조합 짜기
    for order in orders:
      order_combinations = combinations(list(order),count) # 조합 짜기

      for combination in order_combinations:
        # 조합 문자열로 정제
        combination_str = ''.join(sorted(combination))
        if combination_str in count_dict:
          count_dict[combination_str] += 1
        else:
          count_dict[combination_str] = 1

    # value가 2개 이상, max값 인 key를 return
    for k, v in count_dict.items():
      if v >= 2 and v == max(count_dict.values()):
        answer.append(k)
  
  return sorted(answer)


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])

#["AC", "ACDE", "BCFG", "CDE"]