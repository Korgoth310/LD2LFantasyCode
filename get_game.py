def get_game(match_id):
    import od_python

    # create an instance of the API class
    api_instance = od_python.MatchesApi()

    api_response = api_instance.matches_match_id_get(match_id)

    players = api_response.players

    game_stats = [dict() for player in range(len(players))]

    for player in range(len(players)):
        cur_player = players[player]
        name = cur_player.personaname
        kills = cur_player.kills
        deaths = cur_player.deaths
        last_hits = cur_player.last_hits + cur_player.denies
        gpm = cur_player.gold_per_min
        towers = cur_player.tower_kills
        rosh_kills = cur_player.roshan_kills
        obs_placed = cur_player.obs_placed
        stacks = cur_player.camps_stacked
        runes = cur_player.rune_pickups
        stuns = cur_player.stuns

        if cur_player.is_radiant == True:
            denom = api_response.radiant_score
        else:
            denom = api_response.dire_score

        kill_participation = (cur_player.kills + cur_player.assists)/denom

        if cur_player.kills_log[0].time == api_response.first_blood_time:
            first_blood = 1
        else:
            first_blood = 0

        points = 0.3*kills - (3-0.3*deaths) + 0.003*last_hits + 0.002*gpm + 1*towers + 1*rosh_kills + 3*kill_participation + 0.5*obs_placed + 0.5*stacks + 0.25*runes + 4*first_blood + 0.05*stuns
        points = round(points, 2)
        game_stats[player] = {'player_name' : name,
                            'match_id' : match_id,
                            'points' : points,
                            'kills' : kills,
                            'deaths' : deaths,
                            'last_hits' : last_hits,
                            'gold_per_min' : gpm,
                            'towers' : towers,
                            'rosh_kills' : rosh_kills,
                            'kill_participation' : round(kill_participation, 2),
                            'wards_placed' : obs_placed,
                            'camps_stacked' : stacks,
                            'runes' : runes,
                            'first_blood' : first_blood,
                            'stuns' : round(stuns, 2)}

    return game_stats