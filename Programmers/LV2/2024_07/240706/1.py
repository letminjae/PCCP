# 카카오 1차 - 캐시

def solution(cacheSize, cities):
    time = 0
    cache = []
    if cacheSize == 0: 
        return len(cities) * 5
    else:
      for city in cities:
          city = city.lower()
          # 캐시에 같은 도시가 있다면, 삭제 후 다시 도시 추가
          if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
          # 캐시에 같은도시가 없다면
          else:
            # 캐시가 가득 찬 경우는 맨 첫번째 캐시 삭제
            if len(cache) == cacheSize: 
               cache.pop(0)
            cache.append(city)
            time += 5
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))