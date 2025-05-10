# 베스트 앨범

from collections import defaultdict

def solution(genres, plays):
  genres_count = {}
  
  for i in range(len(genres)):
    genre = genres[i]
    play = plays[i]
    if genre not in genres_count:
      genres_count[genre] = play
    else:
      genres_count[genre] += play
  
  # 총 재생횟수 많은 순으로 장르 정렬
  sorted_genres_count = sorted(genres_count.keys(), key=lambda x: genres_count[x], reverse=True)
  
  # 장르별 (고유 번호, 재생횟수) 저장
  genre_dict = defaultdict(list)
  for i, (genre, play) in enumerate(zip(genres, plays)):
    genre_dict[genre].append((i, play))
  
  # 재생 횟수가 많은 곡부터 정렬하되, 재생 횟수가 같으면 고유번호가 작은 순서대로 정렬
  for genre in genre_dict:
    genre_dict[genre].sort(key=lambda x: (-x[1], x[0]))
    
  # 정답 정렬
  answer = []
  for genre in sorted_genres_count:
    for song in genre_dict[genre][:2]:
      answer.append(song[0])
      
  return answer
  
solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])
# [4, 1, 3, 0]