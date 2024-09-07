from collections import Counter

def solution(participant, completion):
    participant_a = Counter(participant)
    completion_a = Counter(completion)
    
    a = participant_a - completion_a
    
    answer = list(a.keys())[0]
    
    return answer