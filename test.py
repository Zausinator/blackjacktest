#Test

import os
import random


def shuffle():
    faces = [['clubs', [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']],
        ['spades', [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']],
        ['hearts', [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']],
        ['diamonds', [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']]]
    cards = []
    for i in range(4):
        for j in range(13):
            cards.append([faces[i][0], faces[i][1][j]])
    random.shuffle(cards)
    return cards

def deal(cards, amount=1, deck = None):
    if deck == None:
        hand = []
    else:
        hand = deck
    a = amount
    for i in range(a):
        card = cards.pop()
        hand.append(card)
    return hand

def value(hand):
    values = []
    for i in range(len(hand)):
        j = hand[i][1]
        if j == 'J' or j == 'Q' or j == 'K':
            card_value = 10
        elif j == 'A':
            if int(sum(values)) > 10:
                card_value = int(1)
            else:
                card_value = int(11)
        else:
            card_value = int(hand[i][1])
        values.append(card_value)
    return int(sum(values))

firstshuffle = shuffle()

mhand = deal(firstshuffle, amount = 2)

mvalue= (value(mhand))


print(mhand)

while mvalue <17:
    deal(firstshuffle, amount = 1, deck = mhand)
    print('hello')
    print(mhand)
    mvalue = value(mhand)
    print(mvalue)


count = 0
starting_money = 200
while starting_money > int(0):
    shufdeck = shuffle()
    if count == 0:
        print('\n\n\t\tWelcome to a new round of blackjack! Good luck!\n\n')
    else:
        print('\n\n\t\t New Round! Let\'s go!\n\n')
    place_bet = int(input('Place your bet! (Minimum 20$)'))
    while place_bet<20:
        print('\n\n\t\tWhat part about \"Minimum 20$\" didn\'t you get?\n\n')
        place_bet = int(input('Place your bet! (Minimum 20$)'))
    while place_bet >starting_money:
        print('\n\n\t\tBro, you don\'t have that type of money.\n\n')
        place_bet = int(input('Place your bet! (Minimum 20$)'))

    inter_money = starting_money - place_bet
    #Now we begin
    print('\n\n\t\t Alright, let\'s go! Good luck.\n\n')
    #shuffle1 = shuffle()
    #fr = first_round(shuffle1)
    #ev = eval(fr[1], fr[2], shuffle1, bet=int(place_bet))
    #print(ev[0])
    #starting_money = inter_money + ev[1]

    #play_again = str(input('\n\n\t\t Do you '+\
    #                        'want to play again?(Y/N)'))
    #if play_again =
    count+=1
