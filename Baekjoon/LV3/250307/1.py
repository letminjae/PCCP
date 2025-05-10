# 여행경로

from collections import defaultdict

def solution1(tickets):
    ticket_dict = defaultdict(list)
    
    # default dict로 key : 출발지, value : 목적지 딕셔너리 생성
    for start, end in tickets:
        ticket_dict[start].append(end)

    for key in ticket_dict:
        ticket_dict[key].sort()

    answer = []
    path = ["ICN"] # 출발 지점에서 계속 어디로 가는지 저장하는 리스트

    while path:
        now = path[-1] # 첫번째는 인천, "ICN"

        # 더이상 갈곳이 없다. 깊이가 끝까지 갔다면, answer에 path의 마지막을 넣어주고 path는 pop
        if now not in ticket_dict or len(ticket_dict[now]) == 0:
            answer.append(path.pop())
        else:
            # 갈 수 있는 곳이 있다면, 경로에 추가하고, ticket_dict에서 pop
            path.append(ticket_dict[now].pop())
    
    # 역순으로 들어오기에 역으로 출력
    return answer[::-1]

# solution1([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# ["ICN", "JFK", "HND", "IAD"]

# 반례로 인해 우선순위 큐를 사용한 방법으로 다시 풀어보기
from collections import defaultdict
import heapq

def solution(tickets):
    ticket_dict = defaultdict(list)

    # 그래프 생성 (우선순위 큐 사용) -> 자동으로 오름차순되어 push
    for start, end in tickets:
        heapq.heappush(ticket_dict[start], end)

    path = []
    
    def dfs(node):
        while ticket_dict[node]:  # 현재 공항에서 갈 수 있는 공항이 남아있다면
            next_node = heapq.heappop(ticket_dict[node])  # 가장 작은 알파벳 먼저 방문
            dfs(next_node)  # 깊이 탐색
        path.append(node)  # dfs로 더 이상 갈 곳이 없을 때 현재 공항을 기록

    dfs("ICN")
    return path[::-1]  # 최종 경로는 역순으로 반환

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])