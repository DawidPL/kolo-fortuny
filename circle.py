import random
possible_field = {'BANKRUT':0, '-50%': -50, '100': 100, '200': 200, '300':300, '500':500, '1000':1000, '1500':1500, '2000':2000}
probability_list = [random.choice(list(possible_field)) for i in range(25)]
def user_point_field():
    user_field = random.choice(probability_list)
    return user_field
