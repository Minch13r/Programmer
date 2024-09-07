def solution(nums):
    max_selectable = len(nums) // 2
    unique_pokemon = len(set(nums))
    return min(max_selectable, unique_pokemon)
# N/2마리의 폰켓몬과 중복 제거한 폰켓몬 종류 중 최소 값 반환