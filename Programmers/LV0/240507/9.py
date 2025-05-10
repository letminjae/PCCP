# 치킨 쿠폰

def solution(chicken):
  answer = 0
  while chicken >= 10:
    service = chicken // 10
    coupon = chicken % 10
    answer += service
    chicken = service + coupon
  return answer