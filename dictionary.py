# dictionary as a HASH implemented by PYTHON


def solution(clothes):
    
    d = dict()
    temp = 1
    for c,i in clothes :     // 2차원 배열 표현식. i 에는 각 2차원 배열의 2번째 요소를 뜻한다.
        if i not in d :
            d[i] = 1 
        else:
                d[i] += 1 
    
    for i in d :
        temp = temp * (d[i]+1)   
    temp -= 1 
        
    return temp
    
    
    
    
    https://programmers.co.kr/learn/courses/30/lessons/42578 문제 출처
