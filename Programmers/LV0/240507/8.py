# 전국 대회 선발 고사

def solution(rank, attendance):
  answer = 0
  realrank = []
  for i in range(len(rank)):
    if attendance[i] == True:
      realrank.append(rank[i])
  realrank.sort()
  for i in rank:
    if i == realrank[0]:
      answer += 10000*rank.index(i)
    elif i == realrank[1]:
      answer += 100*rank.index(i)
    elif i == realrank[2]:
      answer += rank.index(i)
  return answer