def solution(numbers):
    results = [-1] * len(numbers)
    for i in range(len(numbers)-1):
        values = numbers[i]
        for j in numbers[i+1:]:
            if values < j:
                results[i] = j
                break
    
    return results