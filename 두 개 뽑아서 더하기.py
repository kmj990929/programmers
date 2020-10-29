from itertools import permutations

def solution(numbers):
    answer = []
    permute = permutations(numbers,2)
    for a,b in permute:
        answer.append(a+b)
    answer = list(set(answer))
    answer.sort()

    return answer