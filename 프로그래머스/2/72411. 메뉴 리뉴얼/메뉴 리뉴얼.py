from itertools import combinations
from collections import Counter

def solution(orders, course):
    # 주문 목록을 알파벳 순으로 정렬
    sorted_orders = [''.join(sorted(order)) for order in orders]
    
    result = []
    
    # 코스 크기별로 계산
    for c in course:
        # 각 코스 크기에서 나올 수 있는 조합 저장
        combinations_list = []
        for order in sorted_orders:
            combinations_list.extend(combinations(order, c))
        
        # 조합 빈도 계산
        combination_count = Counter(combinations_list)
        
        # 가장 많이 주문된 횟수 찾기 (최소 2번 이상)
        if combination_count:
            max_count = max(combination_count.values())
            if max_count >= 2:
                # 가장 많이 나온 조합들을 결과에 추가
                result += [''.join(combo) for combo, count in combination_count.items() if count == max_count]
    
    # 결과를 사전 순으로 정렬하여 반환
    return sorted(result)
