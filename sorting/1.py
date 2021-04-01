def solution(array, commands):
    answer = []
    
    
    for i in range(len(commands)):
        number = []
        for j in range(commands[i][0] - 1, commands[i][1]):
            number.append(array[j])
        number.sort()
        answer.append(number[commands[i][2] - 1])
    return answer
