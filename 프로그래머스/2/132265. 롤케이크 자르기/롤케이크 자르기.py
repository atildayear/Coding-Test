from collections import Counter

def solution(topping):
    answer = 0
    bro = set()             # 동생이 가진 토핑 종류
    cheolsu = {}
    for t in topping:
        if t in cheolsu:
            cheolsu[t] += 1
        else:
            cheolsu[t] = 1

    for t in topping:
        bro.add(t)         # 현재 토핑을 동생의 집합에 추가
        cheolsu[t] -= 1    # 해당 토핑의 개수를 1 감소시킴

        if cheolsu[t] == 0: # 만약 해당 토핑의 개수가 0이 되면
            del cheolsu[t]  # 해당 토핑을 cheolsu에서 삭제
            
        # 공평하게 나눌 수 있는 경우 체크
        if len(bro) == len(cheolsu):
            answer += 1

    return answer