def solution(n):
    prime = []  # 소수를 저장할 리스트

    # 2부터 n-1까지의 숫자(a)에 대해 반복
    for a in range(2, n+1):
        # number가 소수인지 확인
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:  # 나머지 값이 0이면 소수가 아님
                break  # 소수가 아님, 루프 중단
        else:
            # for 루프가 break 없이 끝나면 소수
            prime.append(a)
    
    answer = len(prime)  # 소수의 개수 반환
    return answer

