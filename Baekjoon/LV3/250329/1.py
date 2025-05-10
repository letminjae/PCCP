# 단속카메라

def solution(routes):
    camera_count = 0
    camera_position = -30001 # -30000 ~ 30000
    # 나가는 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    for route in routes:
      start, end = route[0], route[1]
      # 카메라가 설치된 위치가 차량의 진입 지점보다 작으면 카메라를 설치
      if camera_position < start:
        camera_count += 1
        camera_position = end
        
    return camera_count
  
solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]) # 2