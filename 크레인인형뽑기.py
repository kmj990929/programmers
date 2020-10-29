def solution(board, moves):
    answer = 0
    box = []
    transpose = list(map(list, zip(*board))) #transpose 다시 보기
    for move in moves:
        current = transpose[move-1]
        for i, element in enumerate(current):
            if element != 0:
                current[i] = 0
                if len(box) >= 1 and box[-1] == element:
                    box = box[:-1]
                    answer += 2    
                else:
                    box.append(element)
                break
        
    return answer