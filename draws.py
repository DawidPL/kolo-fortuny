import players as ps
import circle as ce
import assets.strings as ss
import assets.questions as qs

class Draws:
    def random_field(self):
        import main
        if main.players_number == 1:
            print('Koło wylosowało...{}' .format(ce.user_point_field()))
            if ce.user_point_field() == 'BANKRUT' or ce.user_point_field() == '-50%':
                print(ss.field_info)
            else:
                letter_input = input('{} podaj spółgłoskę: '.format((str(ps.players_active[0]))))
                if letter_input not in qs.title.:
                    print(ss.no_letter)
                else:
                    while ce.user_point_field() != ('BANKRUT' or '-50%') or letter_input in qs.title.word_pick().letter_in:
                        ce.user_point_field()
                        print('Grasz o {} zł' .format(ce.user_point_field()))
        elif main.players_number == 2:
            for i in range(len(ps.players_active)):
                pass
draws = Draws()

