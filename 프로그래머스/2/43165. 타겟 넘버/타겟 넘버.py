def solution(numbers, target):
    # 재귀 함수 정의
    def dfs(idx, current_sum):
        # 모든 숫자를 다 사용했을 때
        if idx == len(numbers):
            # 현재 합계가 타겟과 같으면 1을 반환
            if current_sum == target:
                return 1
            else:
                return 0
        else:
            # 현재 숫자를 더한 경우와 뺀 경우를 각각 탐색
            return dfs(idx + 1, current_sum + numbers[idx]) + dfs(idx + 1, current_sum - numbers[idx])
    
    # 처음 재귀 호출 (0번째 인덱스부터 시작, 초기 합은 0)
    return dfs(0, 0)

     # numbers 배열과 target을 입력 받음
    numbers = list(map(int, input().split()))
    target = int(input())
    
    # 결과 출력
    result = solution(numbers, target)
    print(result)
