'''
Programmers - 하샤드 수
https://programmers.co.kr/learn/courses/30/lessons/12947
'''

def solution(n):
    return True if n%sum([int(i) for i in list(str(n))])==0 else False