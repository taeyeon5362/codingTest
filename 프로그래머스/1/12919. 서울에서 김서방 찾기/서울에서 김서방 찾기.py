def solution(seoul):
    answer = ''
    for i, v in enumerate(seoul) :
        if 'Kim' in v :
            answer += '김서방은 ' + str(i) + '에 있다'
            
    return answer