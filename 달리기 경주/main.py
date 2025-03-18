def solution(players, callings):
    player_dict = {i: name for i, name in enumerate(players)}
    name_to_index = {name: i for i, name in enumerate(players)}

    for name in callings:
        index = name_to_index[name]
        if index > 0:  # 이미 선두가 아닌 경우만 변경
            prev_name = player_dict[index - 1]

            # Swap in both dictionaries
            player_dict[index], player_dict[index - 1] = player_dict[index - 1], player_dict[index]
            name_to_index[name] -= 1
            name_to_index[prev_name] += 1

    return [player_dict[i] for i in range(len(players))]