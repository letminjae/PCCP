import math

def time_to_minutes(time_str):
  hours, minutes = map(int, time_str.split(':'))
  return hours * 60 + minutes

def solution(fees, records):
  record_dict = {}
  all_time_dict = {}
 
  for record in records:
    # 기록 정제
    entry_and_exit = record.split(' ')[2] # 입출차 여부, "IN", "OUT"
    car_number = record.split(' ')[1] # 차량 번호
    time = time_to_minutes(record.split(' ')[0])
    # 입차 - 차량번호:입차시간을 record_dict에 저장
    if entry_and_exit == "IN":
      record_dict[car_number] = time
      print(f"record dict - {record_dict}") # 딕셔너리 확인용
    # 출차 - 차량번호:출차시간-입차시간 값을 time_dict에 저장 후, record_dict에서 차량번호 삭제
    if entry_and_exit == "OUT":
      if car_number not in all_time_dict:
        all_time_dict[car_number] = time - record_dict[car_number]
      else:
        all_time_dict[car_number] += time - record_dict[car_number]
      del(record_dict[car_number])
      print(f"time dict - {all_time_dict}") # 딕셔너리 확인용
  # 출차 기록이 없고 입차 기록만 있을 때
  if len(record_dict) != 0:
    print(True)
    for key in record_dict:
      if key in all_time_dict.keys():
        all_time_dict[key] += time_to_minutes("23:59") - record_dict[key]
      else:
        all_time_dict[key] = time_to_minutes("23:59") - record_dict[key]
  # 차량번호 낮은순으로 정렬
  all_time_dict = dict(sorted(all_time_dict.items(), key=lambda x:x[0]))
  print(f"recorded dict - {record_dict}")
  print(f"all time dict - {all_time_dict}")
  # 주차요금 계산 (올림 주의)
  answer = []
  for time in all_time_dict.values():
    if time > fees[0]:
      answer.append(fees[1] + (math.ceil((time - fees[0]) / fees[2])) * fees[3] )
    else:
      answer.append(fees[1])

  return answer


solution([1, 461, 1, 10],["00:00 1234 IN"])