# 네트워크 (깊이/너비 우선탐색 - DFS/BFS)

# DFS로 풀었을 때
def solution1(n, computers):
  answer = 0
  visited = [False] * n

  def dfs(temp):
    visited[temp] = True
    print(f'visited {temp}')
    for i in range(n):
      if computers[temp][i] == 1 and not visited[i]:
        dfs(i)

  for i in range(n):
    if not visited[i]:
      answer += 1
      dfs(i)

  return answer

solution1(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2

# BFS로 풀었을 때
def solution2(n, computers):
  answer = 0
  visited = [False] * n

  def bfs(temp):
    queue = [temp]
    visited[temp] = True
    print(f'visited {temp}')
    while queue:
      temp = queue.pop(0)
      for i in range(n):
        if computers[temp][i] == 1 and not visited[i]:
          queue.append(i)
          visited[i] = True
          print(f'visited {i}')

  for i in range(n): # 0, 1, 2
    if not visited[i]:
      answer += 1
      bfs(i)

  return answer

solution2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
