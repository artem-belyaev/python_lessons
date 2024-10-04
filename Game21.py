import random

# Константы
MIN_CARD_VALUE = 3
MAX_CARD_VALUE = 500
MAX_SCORE = 5000
MORE_WORD = 'Q'
WIN_WORD = 'победил'
LOSE_WORD = 'проиграл'
DRAW_WORD = 'ничья'

player_score = random.randint(MIN_CARD_VALUE,MAX_CARD_VALUE)
print('твоя карта:')
print(player_score)

casino_score = random.randint(MIN_CARD_VALUE,MAX_CARD_VALUE)
print('я сходил')

action = MORE_WORD

while action == MORE_WORD and player_score <= MAX_SCORE and casino_score <= MAX_SCORE:
    action = input('ваш ход:')
    player_score += random.randint(MIN_CARD_VALUE,MAX_CARD_VALUE)
    print(player_score)
    casino_score += random.randint(MIN_CARD_VALUE,MAX_CARD_VALUE)
    print('я сходил')

if (casino_score == player_score) or (player_score > MAX_SCORE and casino_score > MAX_SCORE):
    print(DRAW_WORD)
elif player_score >MAX_SCORE:
    print(LOSE_WORD)
elif casino_score > MAX_SCORE:
    print(WIN_WORD)
elif casino_score > player_score:
    print(LOSE_WORD)
elif player_score == MAX_SCORE:
    print(WIN_WORD)
else:
    print(WIN_WORD)


print(casino_score)










