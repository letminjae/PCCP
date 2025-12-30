# 15649 - N과 M 1
# 라이브러리 말고 백트래킹으로 풀어보기
# 코딩에서는 백트래킹을 재귀 함수와 상태 되돌리기로 구현

"""
# 백트래킹 기본 템플릿
def backtrack(현재_상태):
    # 1. 종료 조건: 정답을 찾거나 더 이상 갈 수 있는 길이 없을 때
    if (종료 조건):
        # 정답을 처리하거나 기록하고 함수 종료
        return

    # 2. 선택지 순회
    for 선택지 in (가능한_선택지들):
        # 3. 가지치기 (Pruning): 이 선택지가 정답이 될 가능성이 있는지 확인
        if (선택지가 유효한 경우):
            # 4. 선택: 상태를 업데이트 (예: visited[선택지] = True)
            backtrack(다음_상태) # 5. 탐색: 재귀 호출로 다음 단계로 넘어감
            # 6. 되돌리기: 재귀 호출이 끝난 후, 상태를 원래대로 되돌림
            # (예: visited[선택지] = False)
"""

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 (수열은 순서가 있다)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * (N+1)
answer = []

def backtrack(count):
    # 종료 조건 : 정답 또는 막다른 길일 때
    if count == M:
        print(*answer)
        return
    
    # 선택지 순회
    for i in range(1, N+1):
        # 가지치기 : 선택지가 정답이 되는지 확인
        if not visited[i]:
            # 1. 선택 - 숫자를 선택하고 사용했음을 표시
            visited[i] = True
            answer.append(i)
            
            # 2. 탐색 - 다음 숫자 호출을 위해 재귀 호출
            backtrack(count+1)
            
            # 3. 되돌리기 - 탐색을 끝내고 현재 숫자를 버리고 상태를 되돌림
            visited[i] = False
            answer.pop()

backtrack(0)