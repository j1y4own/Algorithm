def solution(s):
    answer = []
    change_cnt = 0
    zero_cnt = 0 
    
    
    while True :
        if s == '1':
            break
        else :
            zero_cnt += s.count('0')
            s = s.replace('0', '')
            s = (format(len(s), 'b'))
            change_cnt += 1
            
    answer = [change_cnt, zero_cnt]
            
    return answer