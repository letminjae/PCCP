# 방금 그 곡 - 카카오 3차

# 시간을 분으로 만들기
def time_to_minutes(start_time, end_time):
  start_hour, start_minute = map(int, start_time.split(":"))
  end_hour, end_minute = map(int, end_time.split(":"))
  duration = (end_hour - start_hour) * 60 + (end_minute - start_minute)
  return duration

# 샵을 소문자로 변환
def convert_sharp_notes(melody):
    return (melody.replace("C#", "c")
                  .replace("D#", "d")
                  .replace("F#", "f")
                  .replace("G#", "g")
                  .replace("A#", "a")
                  .replace("B#", "b")) # 설명 잘못 기재로 B# 추가

def solution(m, musicinfos):
    answer = None
    m = convert_sharp_notes(m)
    max_duration = -1 # 재생시간이 제일 긴 곡 찾기
    musicinfos = [info.split(",") for info in musicinfos]
    
    for info in musicinfos:
      start_time, end_time, title, music = info
      duration = time_to_minutes(start_time, end_time)
      converted_music = convert_sharp_notes(music)
      # duration 길이만큼 슬라이스하기 - converted_music이 빈 문자열이라면? Error 발생
      music_repeat = (converted_music * (duration // max(1, len(converted_music)) + 1))[:duration]
      
      if m in music_repeat and duration > max_duration:
            answer = title
            max_duration = duration
      elif m in music_repeat and duration == max_duration:  # 같은시간이면 먼저 나온 것 선택
            continue  # 이미 answer에 저장된 곡이 먼저 나온 곡이므로 유지

    return answer if answer else "(None)"
    
solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# "HELLO"