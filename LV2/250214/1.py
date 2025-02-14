#카카오 코딩테스트 - 오픈채팅방

#실패케이스 (시간복잡도 실패)

def solutionFAIL(records):
  answer = []
  already_enter_dict = {}
  nickname_dict = {}
 
  for record in records:
    # 기록 정제
    state = record.split(" ")[0] # Enter, Leave, Change 상태값
    id = record.split(" ")[1] # 아이디
   
    # Enter 상태일 때
    if state == "Enter":
      nickname = record.split(" ")[2] # 닉네임
      nickname_dict[id] = nickname
      answer.append(f"{id}님이 들어왔습니다.")
     
    # Leave 상태일 때
    if state == "Leave":
      already_enter_dict[id] = True
      answer.append(f"{id}님이 나갔습니다.")

    # Change 상태일 때
    if state == "Change":
      nickname = record.split(" ")[2] # 닉네임
      nickname_dict[id] = nickname

  # nickname_dict 값과 answer id 매칭하여 replace
  updated_answer = []
  for item in answer:
    for uid in nickname_dict:
      print(f'item: {item}, uid: {uid}')
      if uid in item:
        item = item.replace(uid, nickname_dict[uid])
    print(f'update-item: {item}')
    print("----------------------")
    updated_answer.append(item)

  return updated_answer

solutionFAIL(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 실패 이유는 이중for문 때문이지만, 코드가 더러워서 문제를 새롭게 풀었다.

def solution(records):
  answer = []
  nickname_dict = {}
 
  for record in records:
    # 기록 정제
    state, id, *nickname = record.split(" ")
   
    # Enter 상태일 때
    if state == "Enter":
      nickname_dict[id] = nickname[0]
      answer.append((id, '님이 들어왔습니다.'))
    # Leave 상태일 때
    elif state == "Leave":
      answer.append((id, '님이 나갔습니다.'))
    # Change 상태일 때
    elif state == "Change":
      nickname_dict[id] = nickname[0]

  updated_answer = []
  # -> 새로운 시간복잡도 케이스 고려 O(n)
  for id, message in answer:
    updated_answer.append(f"{nickname_dict[id]}{message}")

  return updated_answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]