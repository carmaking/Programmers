def solution(n, lost, reserve):
    answer = 0
    
    reser_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)
    
    for i in reser_del:
        if i - 1 in lost_del:
            lost_del.remove(i-1)
            continue
        elif i + 1 in lost_del:
            lost_del.remove(i+1)
            
    answer = n - len(lost_del)
    
    return answer
