'''
Programmers - 같은 숫자는 싫어
https://programmers.co.kr/learn/courses/30/lessons/12906
'''

import itertools

def solution(arr):
    return list(map(int, (''.join(map(str, (i for i, _ in itertools.groupby(arr)))))))
