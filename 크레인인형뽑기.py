def solution(board, moves):
    answer = 0
    box = []
    transpose = list(map(list, zip(*board))) #transpose 다시 보기
    for move in moves:
        current = transpose[move-1]
        for i, element in enumerate(current):
            if element != 0:
                current[i] = 0
                box.append(element)
    print(box)
    #box check
    idx = 0
    while idx == len(box):
        if box[idx] == box[idx+1]:
            box = box[:idx]+box[idx+2:]
            idx -=1
            answer += 1
        idx += 1
        
    return answer