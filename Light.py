def solution(A):
    count = 0
    l = len(A)
    v = [0 for i in range(l+1)]
    v[0] = 1
    print(v)
    for i,bulb in enumerate(A):
        if v[bulb] == 0:
            v[bulb] = 1
            flag = True
            for j in range(bulb):
                if v[j] == 1:
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                count += 1

    return count



print(solution([1,3,4,2,5]))
