# n진수 게임 (카카오 블라인드 채용)

def convert_number(n, base):
    # 16진수까지 진수변환
    temp = '0123456789ABCDEF'
    # 몫, 나머지
    q, r = divmod(n, base)
    if q == 0:
        return temp[r]
    else:
        return convert_number(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''
    cnt = 0

    while True:
        answer += convert_number(cnt, n)

        if len(answer) >= t * m:
            answer = answer[:t*m]
            return answer[p-1:t * m:m]
        cnt += 1