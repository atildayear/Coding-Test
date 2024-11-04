from collections import deque

def solution(topping):
    # 철수가 처음에 모든 토핑을 가지고 시작합니다.
    cheolsu = {}
    for t in topping:
        if t in cheolsu:
            cheolsu[t] += 1
        else:
            cheolsu[t] = 1
    
    # 동생의 토핑 딕셔너리 초기화
    bro = {}
    topping = deque(topping)
    answer = 0

    # 토핑을 하나씩 옮겨가면서 확인
    while topping:
        # 철수의 토핑에서 하나를 뺍니다.
        t = topping.popleft()
        cheolsu[t] -= 1
        if cheolsu[t] == 0:
            del cheolsu[t]

        # 동생의 토핑에 추가합니다.
        if t in bro:
            bro[t] += 1
        else:
            bro[t] = 1

        # 공평하게 나눠진 경우를 체크
        if len(cheolsu) == len(bro):
            answer += 1
        
        # 동생의 토핑 종류가 철수보다 많아지면 종료
        if len(bro) > len(cheolsu):
            break

    return answer

