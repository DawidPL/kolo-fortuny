import players as ps
import assets.questions as qs
import assets.strings as ss
import draws as ds

players_number = int(input(ss.players_input))
def game_start():
    if players_number:
        print('Podaj imiona {} graczy: '.format(players_number))
        players_list = [str(input()).capitalize() for i in range(players_number)]
        if len(players_list) == 3:
            print(ss.start_game_info)
            print(*players_list, sep=', ')
        elif len(players_list) == 2:
            players_list.append(ps.players_bots[0])
            print(ss.start_game_info)
            print(*players_list, sep=', ')
        else:
            players_list.extend(ps.players_bots)
            print(ss.start_game_info)
            print(*players_list, sep=', ')
        ps.players_active.extend(players_list)
        print(qs.category_pick)
        print(qs.word_shuffle)
        ds.random_field()

game_start()


