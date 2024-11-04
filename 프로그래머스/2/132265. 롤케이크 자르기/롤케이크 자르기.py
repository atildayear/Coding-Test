from collections import deque

def solution(topping):
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
        # 철수의 토핑에서 하나빼서
        t = topping.popleft()  # t에 저장
        cheolsu[t] -= 1 #해당 토핑 갯수 줄이기
        if cheolsu[t] == 0:
            del cheolsu[t] #개수가 0이 되면 딕셔너리에서 해당 토핑 제거

        # 동생의 토핑에 추가
        if t in bro:
            bro[t] += 1 #이미 해당 토핑이 있다면 개수 증가
        else:
            bro[t] = 1 #없었다면 1 새로 추가

        # 공평하게 나눠진 경우를 체크
        if len(cheolsu) == len(bro):
            answer += 1
        
        # 동생의 토핑 종류가 철수보다 많아지면 종료
        if len(bro) > len(cheolsu):
            break

    return answer