def solution(brown, yellow):
    answer = []
    a_list = []
    
    if yellow == 1:
        a_list = [1]
    
    if yellow != 1:
        for i in range(1, yellow+1):
            if yellow % i == 0 :
                a_list.append(i)
                
    l = len(a_list)
    
    for i in range(0, l) :
        a = a_list[-(i+1)]
        b = a_list[i]
        if 2*(a+b) + 4 == brown:
            answer = [b+2,a+2]
                   
    return answer