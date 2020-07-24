'''
Programmers - x만큼 간격이 있는 n개의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12954
'''

def solution(x, n):
    if x != 0:
        return list(range(x, x*(n+1), x))
    else:
        return [0 for i in range(n)]