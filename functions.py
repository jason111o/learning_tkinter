from random import randint


########################### BUTTON FUNCTIONS ###############################
# list to pull random phrases/elements from
def button_press_print_random_phrases():
    phrase_list = ['What a goofball!',
                   'You are smart',
                   'You must be confused',
                   "I'm not kidding with you",
                   "You butt smells bad!",
                   "You will come into great riches",
                   "You will excel in your line of work",
                   "I don't think I would suggest that"]
    ran_num = randint(0, len(phrase_list) - 1)
    return phrase_list[ran_num]


def random_directions():
    direction_list = ('top',
                      'bottom',
                      'left',
                      'right')
    ran_num = randint(0, len(direction_list) - 1)
    return direction_list[ran_num]
###############################################################################
