'''
Programmers - 가운데 글자 가져오기
https://programmers.co.kr/learn/courses/30/lessons/12903
'''

def solution(s):
    lst = list(''.join(s))
    middle = len(lst)//2

    return ''.join(lst[middle-1:middle+1]) if len(lst)%2==0 else ''.join(lst[middle])