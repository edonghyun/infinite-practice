def solution(gems):
    answer = [1, len(gems)]
    
    gem_set = set(gems)
    
    left = 0
    if len(gem_set) == 1:
        return [1, 1]
    
    right = 1
    standard = gems[right]
    gem_map = {
        gems[left]: left
    }
    
    while right < len(gems):
        gem_map[
            gems[right]
        ] = right
        if standard == gems[right]:
            standard = sorted(
                gem_map.keys(),
                key=lambda x: gem_map[x]
            )[0]
            left = gem_map[standard]
        
        if len(gem_map.keys()) == len(gem_set):
            answer = [left + 1, right + 1] \
                if right - left < answer[1] - answer[0] \
                    else answer

        right += 1
    return answer