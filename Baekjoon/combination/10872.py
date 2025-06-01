# 10872 팩토리얼

N = int(input())

answer = 1

for i in range(1, N+1):
  answer = answer * i
  
print(answer if N != 0 else 1)