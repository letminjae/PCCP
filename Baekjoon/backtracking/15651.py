import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)
answer = []

def backtrack(count):
    # 종료조건
    if count == M:
        print(*answer)
        return
    
    # 선택지 순회
    for i in range(1, N+1):
         if not visited[i]:
            #  visited[i] = True - 이미 방문한 곳은 가지 않기에 중복이 안됨.
             answer.append(i)

             backtrack(count+1)

             visited[i] = False
             answer.pop()

backtrack(0)