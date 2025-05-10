# 수열과 구간 쿼리 3

def solution(arr, queries):
  for query in queries:
    arr[query[0]], arr[query[1]] = arr[query[1]], arr[query[0]]
  return arr