# 프로그래머스 LV3 - 디스크 컨트롤러
# 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위

import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0])
    waiting_queue = []
    current_time = 0
    total_time = 0
    job_count = 0
    
    # job count 또는 힙큐의 유무 (처음에는 힙큐에 아무것도 없기에)
    while job_count < len(jobs) or waiting_queue:
        
        # 내부 while문 : 시작시간이 현재시간보다 작거나 같으면 디스크 동작 시작 (힙큐에 집어넣는다)
        while job_count < len(jobs) and jobs[job_count][0] <= current_time:
            heapq.heappush(waiting_queue, (jobs[job_count][1], jobs[job_count][0]))
            job_count += 1 # 한개 넣었으니 다음 job 찾아서 올려야하기에 count++
        
        # 이제 힙큐에서 우선순위 작업 빼서 처리    
        if waiting_queue:
            shortest_job = heapq.heappop(waiting_queue)
            during_time, start_time = shortest_job[0], shortest_job[1]
            end_time = current_time + during_time
            total_time += (end_time - start_time)
            current_time += during_time
        # 힙큐가 없다는건 디스크가 놀고있으니 현재시간을 증가
        else:
            current_time += 1
    
    return total_time // len(jobs)

solution([[0, 3], [3, 5], [1, 9]])