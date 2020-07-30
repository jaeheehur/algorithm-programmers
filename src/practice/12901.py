'''
Programmers - 2016년
https://programmers.co.kr/learn/courses/30/lessons/12901
'''

def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = {1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 0:'THU'}
    
    answer = d[(sum(m[:a-1])+b) % 7]
    return answer