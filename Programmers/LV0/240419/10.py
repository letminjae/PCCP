def solution(n, k):
  food = 12000 * n
  beverage = 2000 * k
  service = (n // 10) * 2000
  total = food + beverage - service
  return total