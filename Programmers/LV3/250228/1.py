# 네트워크 (깊이/너비 우선탐색 - DFS/BFS)

# DFS로 풀었을 때
def solution1(n, computers):
  answer = 0
  visited = [False] * n # 방문여부 체크

  def dfs(node):
    visited[node] = True # 방문처리
    print(f'visited {node}')
    for next_node in range(n): # 모든 컴퓨터 확인
      if computers[node][next_node] == 1 and not visited[next_node]: # 연결되어 있고, 방문하지 않은 노드라면
        dfs(next_node)

  for i in range(n):
    if not visited[i]: # visited[i]가
      dfs(i)
      answer += 1

  return answer

solution1(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2

# BFS로 풀었을 때

from collections import deque
def solution2(n, computers):
  answer = 0
  visited = [False] * n

  def bfs(start):
    queue = deque([start])
    visited[start] = True # 시작노드는 방문 처리한다.

    while queue:
      node = queue.popleft() # 현재 노드 deque에서 꺼내기
      print(f'visited node is {node}')
      for i in range(n):
        if computers[node][i] == 1 and not visited[i]: # 연결되어 있고, 방문하지 않은 노드라면
          queue.append(i) # queue에 추가
          visited[i] = True # 방문처리
          print(f'visited {i}')

  for i in range(n): # 0, 1, 2
    if not visited[i]:
      bfs(i)
      answer += 1

  return answer

solution2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
