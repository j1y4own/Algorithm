def solution(numbers):
    answer = []

    for i in range(len(numbers)) :
        x = numbers[i]
        list = numbers[(i+1):]
        num = -1
        for j in range(len(list)):
            if list[j] > x :
                num = list[j]
                break
        answer.append(num)
    
    return answer
