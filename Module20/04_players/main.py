players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


players_list = [(i_player[0], i_player[1], i_results[0], i_results[1], i_results[2])
                for i_player, i_results in players.items()]

print(players_list)
