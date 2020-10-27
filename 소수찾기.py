from itertools import permutations

def solution(numbers):
    answer = 0
    tot_event = []
    number_list = list(numbers)
    for i in range(1,len(number_list)+1):
        events = list(permutations(number_list,i))
        for event in events:
            integer = "".join(event)
            tot_event.append(int(integer))

    for event in set(tot_event):
        answer += prime_number(event)
    return answer

def prime_number(number):
    if number <2:
        return 0
    for i in range(2,number):
        if number % i == 0:
            return 0
    return 1