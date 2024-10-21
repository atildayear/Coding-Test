def solution(users, emoticons):
    # 가능한 할인율
    disc = [10, 20, 30, 40]
    max_sub = 0
    max_sale = 0

    # 모든 이모티콘에 대해 할인율 조합을 만드는 dfs 함수
    def dfs(depth, combo):
        nonlocal max_sub, max_sale
        
        if depth == len(emoticons):
            sub_count = 0
            sales = 0
            for rate, limit in users:
                total = 0
                for i, price in enumerate(emoticons):
                    if combo[i] >= rate:  # 할인율이 기준에 맞을 때만 구매
                        total += price * (100 - combo[i]) // 100
                if total >= limit:
                    sub_count += 1  # 이모티콘 플러스 서비스 가입
                else:
                    sales += total  # 구매한 금액 추가
            
            # 현재 조합이 가장 나은지 확인
            if sub_count > max_sub or (sub_count == max_sub and sales > max_sale):
                max_sub = sub_count
                max_sale = sales
            return

        # 이모티콘마다 할인율을 선택하여 dfs 호출
        for d in disc:
            dfs(depth + 1, combo + [d])

    # DFS 시작
    dfs(0, [])

    return [max_sub, max_sale]