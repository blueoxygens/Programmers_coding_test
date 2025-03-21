def solution(mats, park):
    answer = -1
    for mat in mats:
        for row in range(len(park)):
            for col in range(len(park[0])):
                available_f = False
                if park[row][col] != '-1':
                    continue #시작점이 빈자리가 아닐 경우 스킵
                else:
                    if col + mat > len(park[0]) or row + mat > len(park):
                        continue
                    else:
                        for i in range(row, row+mat):
                            break_f = False
                            for j in range(col, col+mat):
                                if park[i][j] != '-1':
                                    break_f = True
                                    break
                            if break_f:
                                break
                            if i == row+mat-1 and j == col+mat-1:
                                available_f = True
                        if mat > answer and available_f:
                            answer = mat
    return answer