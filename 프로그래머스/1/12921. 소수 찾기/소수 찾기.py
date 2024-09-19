def solution(n):
    if n < 2:
        return 0

    # 소수 여부를 나타내는 불리언 리스트 초기화
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체 구현
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # 소수의 개수 계산
    answer = sum(is_prime)
    return answer