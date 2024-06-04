# PCCE 10번 기출 - 데이터 분석

def solution(datas, ext, val_ext, sort_by):
  answer = []
  data_dict = {
    "code" : 0,
    "date" : 1,
    "maximum" : 2,
    "remain" : 3
    }
  for data in datas:
    value = data[data_dict[ext]]
    if value <= val_ext:
      answer.append(data)

  answer.sort(key = lambda x : x[data_dict[sort_by]])
  return answer


print(solution([[1, 20300104, 100, 80], 
                [2, 20300804, 847, 37], 
                [3, 20300401, 10, 8]],
                "date",
                20300501,
                "remain"))