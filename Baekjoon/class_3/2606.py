import sys
input = sys.stdin.readline
from collections import deque
computer = int(input())
N = int(input())

network = [[] for _ in range(computer+1)] # 2차원 배열
visited = [False for _ in range(computer+1)] # 감염 여부

for _ in range(N):
    start, end = map(int, input().split())
    network[start].append(end)
    network[end].append(start)

def bfs():
    q = deque()
    count = 0
    q.append(1) # 1번부터 시작
    visited[1] = True
    while q:
        cur = q.popleft()
        for val in network[cur]:
            if visited[val] == False:
                q.append(val)
                visited[val] = True
                count += 1
    print(count)

bfs()