def solution(results):
    o_score = 0
    x_score = 0
    
    count = 1
    for i in range(1, len(results)):
        if results[i] == results[i-1]:
            count += 1
        else:
            count = 1
            
        if count == 3:
            if results[i] == 'O':
                o_score = 1
            else:
                x_score = 1
                
            count = 0
    
    if x_score > o_score:
        print("X")
    elif o_score > x_score:
        print("O")
    else:
        print("tie")

solution("XOXXXOOOXOOO")