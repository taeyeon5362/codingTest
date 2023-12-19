def solution(intStrs, k, s, l):
    answer = []
    num = []
    for i in intStrs :
        answer.append(i[s:s+l])
    for i in answer :
        if int(i) > k :
            num.append(int(i))
    return num