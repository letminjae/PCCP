# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length) # 현재 다리 상태
    truck_weights = deque(truck_weights) # pop 최적화를 위해 deque로 변환
    current_weight = 0 # 다리 위 트럭 무게

    while bridge:
        answer += 1 # 1초 씩 증가
        exited_truck = bridge.popleft()
        current_weight -= exited_truck # 다리에서 나갔으니, 무게 빼기

        if truck_weights:
            # 다리무게보다 낮아 다리에 진입이 가능할 때
            if current_weight + truck_weights[0] <= weight:
                entering_truck = truck_weights.popleft() # 다리에 들어왔으니, 대기 트럭에서 빼기
                bridge.append(entering_truck) # 다리에 진입한 트럭 추가
                current_weight += entering_truck  # 다리 무게 갱신
            else:
                bridge.append(0)
                
    return answer


solution(2, 10, [7,4,5,6])