# 이모티콘 할인행사

def solution(users, emoticons):
    answer = [0, 0]

    # 할인율은 10~40%로 고정이다.
    discounts = [10, 20, 30, 40]
    # 모든 할인율에 대한 조합
    discounts_rate = []

    # 이모티콘 할인율 - DFS로 구현
    def dfs(temp, depth):
        # 깊이가 끝까지 도달한다면 discounts_rate에 추가
        if depth == len(temp):
            discounts_rate.append(temp[:])
            return
        for d in discounts:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d

    dfs([0] * len(emoticons), 0)
    
    # 할인율 조합 하나씩 설정
    for dis in range(len(discounts_rate)):
        plus_service = 0
        income = 0

        # 유저 하나하나 확인
        for user in users:
            buying_emoticon = 0
            
            # 구매조건 할인율, 충족 돈 확인
            for i in range(len(emoticons)):
                # 만약 할인율이 users[0]보다 크거나 같다면, 할인된 이모티콘 값 더하기
                if discounts_rate[dis][i] >= user[0]:
                    buying_emoticon += emoticons[i] * ((100 - discounts_rate[dis][i]) * 0.01)
            # buying_emoticon이 충족 돈보다 크거나 같으면, 서비스 구매
            if user[1] <= buying_emoticon:
                plus_service += 1
            # buying_emoticon이 충족 돈보다 작으면, income에 추가
            else:
                income += buying_emoticon
        
        # 서비스 숫자가 answer보다 많으면, 원래대로 저장
        if answer[0] < plus_service:
            answer = [plus_service, int(income)]
        # 서비스 숫자가 answer과 같으면 income보다 작은지까지도 계산
        elif answer[0] == plus_service:
            if answer[1] < income:
                answer = [plus_service, int(income)]

    return answer


solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]) 
# [4, 13860]