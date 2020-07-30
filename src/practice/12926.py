'''
Programmers - 시저 암호
https://programmers.co.kr/learn/courses/30/lessons/12926
'''

def solution(s, n):
    ascii_upper = list(range(65, 91))
    ascii_lower = list(range(97, 123))
    ord_list = [ord(i) for i in list(s)]
    
    answer_list = []
        
    for i in range(len(s)):            
        if ord_list[i] in ascii_lower:
            if (ascii_lower.index(ord_list[i])+n) >= 26:
                answer_list.append(chr(ascii_lower[(ascii_lower.index(ord_list[i])+n)%26]))
            else:
                answer_list.append(chr(ascii_lower[(ascii_lower.index(ord_list[i])+n)]))
                
        elif ord_list[i] in ascii_upper:
            if (ascii_upper.index(ord_list[i])+n) >= 26:
                answer_list.append(chr(ascii_upper[(ascii_upper.index(ord_list[i])+n)%26]))
            else:
                answer_list.append(chr(ascii_upper[(ascii_upper.index(ord_list[i])+n)]))
                
        else:
            answer_list.append(chr(ord_list[i]))
            
    return ''.join(answer_list)