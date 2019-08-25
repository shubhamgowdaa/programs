## soluton 1
# def solution(A):
#     count = 0
#     l = len(A)
#     v = [0 for i in range(l+1)]
#     v[0] = 1
#     print(v)
#     for i,bulb in enumerate(A):
#         if v[bulb] == 0:
#             v[bulb] = 1
#             flag = True
#             for j in range(bulb):
#                 if v[j] == 1:
#                     continue
#                 else:
#                     flag = False
#                     break
#             if flag == True:
#                 count += 1
#
#     return count
#
#
#
# print(solution([1,3,4,2,5]))




def solution(S):
    stack = []
    max_num = 1048576

    S_list = S.split(' ')
    # print(S_list)
    for op in S_list:
        if op[0].isdigit():
            if int(op)>=0 and int(op)< max_num:
                # print(op)
                stack.append(int(op))
            else:
                return -1
        elif op == 'POP':
            if len(stack)>0:
                val = stack.pop()
            else:
                return -1
        elif op == 'DUP':
            if len(stack) > 0:
                val = stack[-1]
                stack.append(val)
            else:
                return -1
        elif op == '+':
            if len(stack) > 1:
                val1 = stack.pop()
                val2 = stack.pop()
                if (val1 + val2) < max_num:
                    stack.append(val1 + val2)
                else:
                    return -1
            else:
                return -1
        elif op == '-':
            if len(stack) > 1:
                val1 = stack.pop()
                val2 = stack.pop()
                if (val1 - val2) >= 0:
                    stack.append(val1 - val2)
                else:
                    return -1
            else:
                return -1
    # print(stack)
    return stack[-1]



# print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
# print(solution("3 DUP 5 - -"))
