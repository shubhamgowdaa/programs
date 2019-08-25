import math
def solution(N,K):
    b = -1
    if N<K:
        return b
    else:
        b = math.factorial(N)/(math.factorial(K)*math.factorial(N-K))
        if b>1000000000:
            b = -1
        return b

print(solution(40,20))
