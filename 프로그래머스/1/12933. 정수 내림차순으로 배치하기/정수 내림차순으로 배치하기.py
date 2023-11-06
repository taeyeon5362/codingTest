def solution(n):
    n = str(n)
    li = []
    for i in n :
        li.append(i)
    li.sort(reverse=True)
    st = ''
    for i in li :
        st += i
    return int(st)