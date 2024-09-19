def solution(n):
    # n+1 길이의 True 리스트 생성 (소수 여부를 표시)
    sieve = [True] * (n + 1)
    
    # 0과 1은 소수가 아니므로 False로 설정
    sieve[0] = sieve[1] = False

    # 2부터 sqrt(n)까지 반복하면서 배수들을 False로 표시
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # i가 소수일 경우
            for j in range(i*i, n + 1, i):  # i의 배수들을 False로 설정
                sieve[j] = False

    # True인 값의 개수를 세서 반환 (소수의 개수)
    return sum(sieve)