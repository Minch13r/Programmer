def solution(arr):
    # 결과를 저장할 리스트 초기화
    answer = []
    
    # 첫 번째 원소는 무조건 추가
    if arr:
        answer.append(arr[0])
    
    # 두 번째 원소부터 마지막 원소까지 순회하면서 처리
    for i in range(1, len(arr)):
        # 이전 원소와 현재 원소가 다를 때만 결과 리스트에 추가
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    
    return answer
