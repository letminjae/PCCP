# 폰켓몬

def solution(nums):
    answer = []
    n = len(nums) // 2
   
    for i in range(len(nums)):
        if len(answer) < n:
            if nums[i] not in answer:
                answer.append(nums[i])
               
    return len(answer)
