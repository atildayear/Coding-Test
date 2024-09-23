def solution(numbers):
    results = [-1] * len(numbers)
    stack = [] #stack 추가
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]]<numbers[i]:
            results[stack.pop()] = numbers[i]
        stack.append(i)
    
    return results