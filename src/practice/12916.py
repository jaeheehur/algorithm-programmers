'''
Programmers - 문자열 내 p와 y의 개수
https://programmers.co.kr/learn/courses/30/lessons/12916
'''

def solution(s):
    lst = list(''.join(s))
    p_cnt, y_cnt = 0, 0
    
    for i in range(len(lst)):
        if lst[i] == 'p' or lst[i] == 'P':
            p_cnt += 1
        elif lst[i] == 'y' or lst[i] == 'Y':
            y_cnt += 1
        else:
            False
    
    return True if p_cnt == y_cnt else False