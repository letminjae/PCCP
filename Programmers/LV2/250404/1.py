# 순위 검색

from collections import defaultdict
from itertools import product
import bisect

def solution(info, query):
    data = defaultdict(list)
    
    for person in info:
        split = person.split()
        items = split[:-1]
        coding_score = int(split[-1])

        # data 딕셔너리에 key-value 조합 짜기
        options = [(item, "-") for item in items]

        for case in product(*options):
            key = ''.join(case)
            data[key].append(coding_score)

    # 점수 리스트 정렬
    for key in data:
        data[key].sort()

    answer = []
    for q in query:
        q = q.replace(" and", "")
        q_parts = q.split()
        q_key = ''.join(q_parts[:-1])
        q_score = int(q_parts[-1])

        # 이분 탐색
        data_coding_score = data.get(q_key, []) # data에서 q_key와 맞는 코딩점수 값 찾기
        idx = bisect.bisect_left(data_coding_score, q_score) # 왼쪽으로 이진 탐색
        answer.append(len(data_coding_score) - idx)
    
    return answer
    

solution(["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]
         )