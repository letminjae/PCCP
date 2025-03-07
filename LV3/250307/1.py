# 여행경로

from collections import defaultdict

def solution(tickets):
    ticket_dict = defaultdict(list)
    
    # default dict로 key : 출발지, value : 목적지 딕셔너리 생성
    for start, end in tickets:
        ticket_dict[start].append(end)

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

    

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# ["ICN", "JFK", "HND", "IAD"]