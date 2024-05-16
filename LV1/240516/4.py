# # PCCP 기출문제 1번 / 붕대감기

def solution(bandage, health, attacks):
    maxhealth = health
    maxtime = attacks[-1][0]
    attack_dict = {}

    for i in attacks:
        attack_dict[i[0]]=i[1]

    time=0
    continue_sec = 0

    # 0초부터 마지막 공격당한 초까지
    while time<=maxtime:
        # time이 공격 초에 있다면: 체력이 깎이고 연속붕대 초기화
        if time in attack_dict:
            health -= attack_dict[time]
            continue_sec=0

            # 체력이 0 이하일 때는 -1 리턴
            if health <=0:
                return -1

        # time이 공격 초에 없다면 : 연속붕대효과 또는 치유
        else:
            continue_sec += 1
            if continue_sec < bandage[0]:
                health += bandage[1]
                if health>maxhealth:
                    health = maxhealth

            else:
                health = health + bandage[1] + bandage[2]
                if health>maxhealth:
                    health = maxhealth
                continue_sec=0

        time+=1

    return health

print(solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]))