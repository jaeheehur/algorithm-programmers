'''
Programmers - 콜라츠 추측
https://programmers.co.kr/learn/courses/30/lessons/12943
'''

def solution(num):
    count = 0

    while (num != 1) & (count>=0):
        # if count is less than 500
        if num%2==0 : num = num//2 
        else: num = (3*num)+1
        count += 1
        
        # if count is more than 500
        if count > 500: count = -1
    
    return count