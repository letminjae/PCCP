# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    N,M = 4,3

    # 왼손, 오른손 엄지
    lsy,lsx = N-1,0
    rsy,rsx = N-1,M-1

    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            for col in range(N):
                for row in range(M):
                    if keypad[col][row] == number:
                        lsy,lsx = col,row

        elif number in [3,6,9]:
            answer += 'R'
            for col in range(N):
                for row in range(M):
                    if keypad[col][row] == number:
                        rsy,rsx = col,row

        elif number in [2,5,8,0]:
            for col in range(N):
                for row in range(M):
                    if keypad[col][row] == number:
                        temp1 = abs(col-rsy)+abs(row-rsx)
                        temp2 = abs(col-lsy)+abs(row-lsx)

                        if temp1 > temp2:
                            lsy,lsx = col,row
                            answer += 'L'

                        elif temp1 < temp2:
                            rsy,rsx = col,row
                            answer += 'R'

                        elif temp1 == temp2:
                            if hand == 'right':
                                answer += 'R'
                                rsy,rsx = col,row
                            else:
                                answer += 'L'
                                lsy,lsx = col,row

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))