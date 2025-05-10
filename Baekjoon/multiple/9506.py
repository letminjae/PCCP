# 9506 약수들의 합

while True:
    N = int(input())

    if N == -1:
        break

    multiple = []
    for i in range(1,N):
        if N % i == 0:
            multiple.append(i)
    
    if sum(multiple) == N:
        print(N, " = ", " + ".join(str(i) for i in multiple), sep="")
    else:
        print(N, "is NOT perfect.")