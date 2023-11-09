def solution(num) :
    binary_num = bin(num)[2:]
    cnt1_num = binary_num.count('1')
    nextnum = num + 1
    cnt1_nextnum = 0

    while True :
        binary_nextnum = bin(nextnum)[2:]
        cnt1_nextnum = binary_nextnum.count('1')
        if cnt1_nextnum == cnt1_num :
            break
        else :
            nextnum += 1

    return nextnum
 