def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    persons = [person1, person2, person3]
    correct_num = [0,0,0]

    #맞은 갯수 count
    for person_i in range(len(persons)):
        person = persons[person_i]
        length = len(person)
        for i in range(len(answers)):
            idx = i % length
            if answers[i] == person[idx]:
                correct_num[person_i] += 1

    #가장 많이 맞춘 사람 answer에 넣기
    max_score = max(correct_num)
    for idx in range(3):
        if max_score == correct_num[idx]:
            answer.append(idx+1)

    return answer