def solution(array, commands):
    answer = []
    
    for i in commands:
        array_list = array[i[0]-1:i[1]]
        array_list.sort()
        answer.append(array_list[i[2]-1])

    return answer