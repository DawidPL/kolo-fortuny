import random
import players as ps
import assets.strings as ss
import assets.questions as qs

possible_field = {'BANKRUT':0, '-50%': -50, '100': 100, '200': 200, '300':300, '500':500, '1000':1000, '1500':1500, '2000':2000}
probability_list = [random.choice(list(possible_field)) for i in range(25)]

def user_point_field():
    user_field = random.choice(probability_list)
    return user_field

def random_field():
    from main import players_number
    if players_number == 1:
        print('Koło wylosowało...{}' .format(user_point_field()))
        if user_point_field() == 'BANKRUT' or user_point_field() == '-50%':
            print(ss.field_info)
        else:
            letter_input = input('{} podaj spółgłoskę: '.format((str(ps.players_active[0]))))
            if letter_input not in qs.word or letter_input.upper() not in qs.word:
                print(ss.no_letter)
            else:
                while user_point_field() != ('BANKRUT' or '-50%') or letter_input in qs.word or letter_input.upper() in qs.word:
                    print('Grasz o {} zł' .format(user_point_field()))
                    qs.word_shuffle = ''.join(('*' if i != letter_input else letter_input for i in qs.word))
                    print(qs.word_shuffle)
                print('teraz gra kolejny zaawodnik')
    '''elif players_number == 2:
        for i in range(len(ps.players_active)):
            pass'''
