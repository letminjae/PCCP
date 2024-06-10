# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    dict_term = dict()
    today_list = list(map(int, today.split('.')))

    for term in terms:
        split_term = term.split()
        dict_term[split_term[0]] = int(split_term[1])*28

    for i in range(len(privacies)):
        date, period = privacies[i].split()
        date_list = list(map(int, date.split('.')))

        year = (today_list[0] - date_list[0])*336
        month = (today_list[1] - date_list[1])*28
        day = today_list[2] - date_list[2]

        if dict_term[period] <= year + month + day:
            answer.append(i+1)

    return answer