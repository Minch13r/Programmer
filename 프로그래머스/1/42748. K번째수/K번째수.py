def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced_array = array[i-1:j]  # i번째부터 j번째까지 자르기 위해 인덱스에 맞게 -1 해줍니다.
        sorted_array = sorted(sliced_array)
        answer.append(sorted_array[k-1])  # k번째 숫자를 구하기 위해 인덱스에 맞게 -1 해줍니다.
    return answer

# 예시 입력
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 함수 호출 및 결과 출력
print(solution(array, commands))  # [5, 6, 3]
