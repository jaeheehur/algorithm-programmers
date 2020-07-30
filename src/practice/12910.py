'''
Programmers - 나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910
'''

def solution(arr, divisor):
    lst = [arr[i] for i in range(len(arr)) if arr[i]%divisor==0]
    if not lst: lst = [-1]
    
    return sorted(lst)