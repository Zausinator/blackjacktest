# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:41:53 2018

@author: Zausi
"""

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

def first_round(shuffleddeck):
    intro = ('\n\n\nWelcome to a new round of blackjack! Good luck!\n\n')

    mhand = deal(shuffleddeck, amount=2)
    dhand = deal(shuffleddeck, amount=2)

    vallist = [intro, mhand, dhand]

    return vallist

def eval(myhand, dealerhand, shuffleddeck, bet = 0, mdone = False):
    mhand = myhand
    mvalue = value(mhand)
    mlen = len(mhand)

    dhand = dealerhand
    dvalue = value(dhand)
    dlen = len(dhand)

    ogb = bet
    if ogb == 0:
        ogb = int(0)
    print('Your cards: \t')
    for i in range(mlen):
        print('\n\t\t%s of %s'%(mhand[i][1], mhand[i][0]))
    print('\n\n(Total value:\t%i)\n\n' %mvalue)
    print('Dealer\'s first card: \n\n\t\t%s of %s'\
                 %(dhand[0][1],dhand[0][0]))

    if dlen > 2:
        print('Dealer\'s next cards:')
        for i in range(dlen):
            if i == 0 or i == int(dlen-1):
                continue
            else:
                print('\n\n\t\t%s of %s'  %(dhand[i][1],dhand[i][0]))

    if dvalue == 21 and mvalue !=21 and mlen == 2:
        result = '\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                 %(dhand[1][1], dhand[1][0]) +'You lost, Sucker!'
        betreturn = int(0)

    elif dhand == 21 and mvalue == 21 and mlen==2:
        result ='\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                %(dhand[1][1],dhand[1][0]) +'Push. You got lucky.'
        betreturn = int(bet)

    elif dvalue != 21 and mvalue == 21 and mlen==2:
        result = '\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                 %(dhand[1][1], dhand[1][0]) +'Blackjack! Congrats!'
        betreturn = 3*int(bet)

    elif int(mvalue)>21:
        result = '\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                 %(dhand[1][1], dhand[1][0]) +'You Bust! You suck!'
        betreturn = int(0)

    elif int(mvalue)<22 and int(dvalue)>21:
        result = '\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                 %(dhand[-1][1], dhand[-1][0]) +'You won! Congrats!'
        betreturn = 2* int(bet)

    elif mdone == True and int(mvalue)<int(dvalue):
        result = '\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                 %(dhand[-1][1], dhand[-1][0]) +'You lost, Sucker!'
        betreturn = int(0)

    elif mdone == True and int(mvalue)>int(dvalue):
        result = '\nDealer\'s final card: \n\n\t\t%s of %s\n\n'\
                 %(dhand[-1][1], dhand[-1][0]) +'You won, congrats!'
        betreturn = 2 * int(bet)

    else:
        result = nextrounds(shuffleddeck, mhand, dhand, bet = ogb)
        betreturn = int(0)

    resultlist = [result, betreturn]
    return resultlist

def nextrounds(cards, mhand, dhand, bet=0):
    b = int(bet)
    hand = mhand
    if value(hand)>21 or value(dhand)>21:
        return None
    elif value(hand)==21:
        nhand = hand
        dvalue = value(dhand)
        while dvalue<17:
            deal(cards, amount=1, deck = dhand)
            dvalue = value(dhand)
        evalnh = eval(nhand, dhand, cards, bet=b, mdone = True)
    else:
        choice = str(input('\n\nDo you want another card?(Y/N)').lower())
        if choice == 'y':
            nhand = deal(cards, amount=1, deck = hand)
            evalnh = eval(nhand, dhand, cards, bet = b)
        else:
            nhand = hand
            nvalue = value(nhand)
            dvalue = value(dhand)
            while dvalue<17:
                deal(cards, amount=1, deck = dhand)
                dvalue = value(dhand)
            while dvalue<=nvalue:
                deal(cards, amount=1, deck = dhand)
                dvalue = value(dhand)
            evalnh = eval(nhand, dhand, cards, bet = b, mdone = True)

        return evalnh


def main():
    count = 0
    starting_money = 200
    while starting_money > int(0):
        shufdeck = shuffle()
        if count == 0:
            print('\n\n\t\tWelcome to a new round of blackjack! Good luck!\n\n')
        else:
            print('\n\n\t\t New Round! Let\'s go!\n\n')
        print('\n\n\t\tYour current money ammount: ' + str(starting_money))
        place_bet = int(input('\n\t\tPlace your bet! (Minimum 20$)'+\
                              '\n\n\t\t'))
        while place_bet<20:
            print('\n\n\t\tWhat part about \"Minimum 20$\" didn\'t you get?\n\n')
            place_bet = int(input('\n\t\tPlace your bet! (Minimum 20$)'))
        while place_bet >starting_money:
            print('\n\n\t\tBro, you don\'t have that type of money.\n\n')
            place_bet = int(input('\n\t\tPlace your bet! (Minimum 20$)'))

        inter_money = starting_money - place_bet
        #Now we begin
        print('\n\n\t\t Alright, let\'s go! Good luck.\n\n')
        shuffle1 = shuffle()
        fr = first_round(shuffle1)
        ev = eval(fr[1], fr[2], shuffle1, bet=int(place_bet))
        for i in range(len(ev[0])):
            if i !=-1:
                print(ev[0][i])
        starting_money = int(inter_money) + int(ev[0][-1])
        print('\n\n\t\tYour current total: ' + str(starting_money))
        if starting_money<=int(0):
            break
        play_again = str(input('\n\n\t\t Do you '+\
                                'want to play again?(Y/N)').lower())
        if play_again == 'y':
            count+=1
        else:
            print('Your final total: ' + str(starting_money))
            break
    if starting_money <= int(0):
        print('\n\n\t\tYou\'re broke!. Come back when you got money.')
    print('\n\n\t\tGoodbye')


print(main())
#shuffle1 = shuffle()

#fr = first_round(shuffle1)
#print(fr[0])
#ev = eval(fr[1], fr[2], shuffle1)

#for i in ev[0]:
    #print(i)
