# 유연근무제

def time_to_minutes(time):
    hour = time // 100
    minute = time % 100
    return hour * 60 + minute

def solution(schedules, timelogs, startday):
    late_worker = set() # 늦은 사람
    
    for i in range(7) : # 1주는 7일
        # 현재 날짜
        current_day = (startday + i - 1) % 7

        # 주말 제외
        if current_day in [5, 6]:
            continue

        for j in range(len(schedules)):
            # 정상출근 시간
            schedule = time_to_minutes(schedules[j]) + 10
            # 실제출근 시간
            timelog = time_to_minutes(timelogs[j][i])

            if timelog > schedule:
                late_worker.add(j)
    
    return len(schedules) - len(late_worker)
    
solution([700, 800, 1100],
         [[710, 2359, 1050, 700, 650, 631, 659], 
          [800, 801, 805, 800, 759, 810, 809], 
          [1105, 1001, 1002, 600, 1059, 1001, 1100]],
         5)