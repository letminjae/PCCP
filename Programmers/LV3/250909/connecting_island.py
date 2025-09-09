# 프로그래머스 LV3 - 섬 연결하기
# 최소 신장 트리 => 크루스칼 알고리즘 : 파인드-유니온 자료구조 사용 (방향이 없는 가중치 그래프)
# 싸이클을 효율적으로 감지하고 방지

def solution(n, costs):
    # 간선 정렬 (비용이 낮은 순)
    costs.sort(key=lambda x:x[2])

    # 노드 생성
    parents = [i for i in range(n)]

    # find - 대표 원소 찾기
    def find(parents, x):
        if parents[x] != x:
            parents[x] = find(parents, parents[x])
        return parents[x]

    # union - 연결된 두 섬을 하나의 섬번호로 변경 (사이클 방지)
    def union(parents, x, y):
        x = find(parents, x)
        y = find(parents, y)

        if x < y:
            parents[y] = x
        else:
            parents[x] = y
    
    answer = 0
    for u,v,c in costs:
        if find(parents, u) != find(parents, v):
            answer += c
            union(parents, u, v)
    
    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])