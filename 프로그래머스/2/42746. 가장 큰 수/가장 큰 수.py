from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    
    return answer
