# PCCP 기출 - 동영상 재생기

def hourToMinutes(time):
    time = time.split(":")
    return int(time[0])*60 + int(time[1])

def minutesToHour(time):
    hour, minutes = str(time//60), str(time%60)
    if len(hour) == 1:
        hour = "0" + hour
    if len(minutes) == 1:
        minutes = "0" + minutes
    return hour + ":" + minutes

def solution(video_len, pos, op_start, op_end, commands):
    video_len = hourToMinutes(video_len)
    pos = hourToMinutes(pos)
    op_start = hourToMinutes(op_start)
    op_end = hourToMinutes(op_end)

    if op_start <= pos <= op_end:
        pos = op_end

    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        elif command == "next":
            pos = min(video_len, pos + 10)
    
        if op_start <= pos <= op_end:
            pos = op_end
    
    return minutesToHour(pos)

solution("07:22","04:05","00:15","04:07",["next"])