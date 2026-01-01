# 17103 골드바흐 파티션

N = int(input())

# 소수 찾기
def seive(n):
    is_prime = [False, False] + [True] * (n-1) # 0, 1은 이미 False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i): # 배수 제거
                is_prime[j] = False
    return is_prime

data = [int(input()) for _ in range(N)]
max_num = max(data)
prime = seive(max_num)

for n in data:
    cnt = 0
    for i in range(2, n//2 +1): # 절반까지만 순회하면 중복방지 가능
        if prime[i] and prime[n-i]:
            cnt += 1
    print(cnt)