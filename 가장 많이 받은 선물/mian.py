def calc_num(diff, num, present_point, A, B):
    if diff > 0:
        return num + 1
    elif diff == 0 and present_point[A] > present_point[B]:
        return num + 1
    return num

def solution(friends, gifts):
    answer = 0
    present_point = [0] * len(friends)
    give_and_take = [[0] * len(friends) for _ in range(len(friends))]

    # 선물 주고받기 기록 저장
    for record in gifts:
        g, r = record.split()
        i, j = friends.index(g), friends.index(r)
        give_and_take[i][j] += 1

    # 선물 지수 계산
    for i, name in enumerate(friends):
        g_count = sum(give_and_take[i])  # 준 선물 개수
        r_count = sum(give_and_take[j][i] for j in range(len(friends)))  # 받은 선물 개수
        present_point[i] = g_count - r_count

    # 다음 달 받을 선물 개수 계산
    for A in range(len(friends)):
        num = 0
        for B in range(len(friends)):
            if A == B:
                continue  # 같은 사람 비교 X

            diff = give_and_take[A][B] - give_and_take[B][A]
            num = calc_num(diff, num, present_point, A, B)

        answer = max(answer, num)  # 최댓값 업데이트

    return answer
