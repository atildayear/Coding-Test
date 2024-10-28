def solution(gems):
    total_gems = len(set(gems))  # 보석의 종류 수
    gem_count = {}  # 현재 구간의 보석 개수를 저장할 딕셔너리
    start, end = 0, 0
    result = [0, len(gems)]  # 최소 구간 초기값 (전체 구간으로 설정)
    
    while end < len(gems):
        # end 포인터를 이동시키며 보석 추가
        gem_count[gems[end]] = gem_count.get(gems[end], 0) + 1
        end += 1
        
        # 모든 종류의 보석을 포함하는 구간이 될 때까지 start 포인터 이동
        while len(gem_count) == total_gems:
            # 현재 구간이 더 짧은 경우 갱신
            if end - start - 1 < result[1] - result[0]:
                result = [start, end - 1]
            
            # start 포인터가 가리키는 보석을 빼고 한 칸 이동
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]  # 개수가 0이 되면 해당 보석 제거
            start += 1
    
    # 진열대 번호는 1번부터 시작하므로 결과에 +2
    return [result[0] + 1, result[1] + 1]
