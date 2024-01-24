def solution(elements):
    ele = set()
    lene = len(elements)
    for i in range(0, lene):
        E = elements[i]
        ele.add(E)
        for j in range(i+1, lene+i):
            E += elements[j%lene]
            ele.add(E)
    return len(ele)

# def solution(elements):
#     ele = []
#     for i in range(0, len(elements)):
#         answer = 0
#         for j in range(i, len(elements)+i):
#             answer += elements[j%len(elements)]
#             if answer not in ele:
#                 ele.append(answer)
#     return len(ele)
