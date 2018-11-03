import os
import random
import numpy as np

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, \
        11, 12, 13, 14]*4


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        '''card = deck.pop()
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"'''
        hand.append(card)
    count = np.sum
    return hand

def hit_me():
    hit = input('Do you wish to add another card?(y/n)')
    if hit == 'y':
        hand.append(card)
    else:
        final_hand = hand

print(deal(deck) + hit_me())
