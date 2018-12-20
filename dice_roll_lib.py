"""
Library for dice rolling

"""

import random


def flip_a_coin():
    """
    this flips a 2-sided coin
    return 0 for tails
    return 1 for heads
    """
    coin_flip = random.randint(0,1)
    return coin_flip

def roll_d4():
    """
    this rolls a 4-sided die and returns the value
    """
    d4 = random.randint(1,4)
    return d4

def roll_d6():
    """
    this rolls a 6-sided die and returns the value
    """
    d6 = random.randint(1,6)
    return d6

def roll_d8():
    """
    this rolls an 8-sided die and returns the value
    """
    d8 = random.randint(1,8)
    return d8

def roll_d10():
    """
    this rolls a 10-sided die and returns the value
    """
    d10 = random.randint(1,10)
    return d10

def roll_d12():
    """
    this rolls a 12-sided die and returns the value
    """
    d12 = random.randint(1,12)
    return d12

def roll_n_sided_die(n):
    """
    this rolls an n-sided die and returns the value
    """
    dice_n = random.randint(1,n)
    return dice_n

def roll_multiple_n_sided_dice(number_of_dice, n):
    """
    This will roll several n-sided die.  How many dice to roll is
    given by "number_of_dice" and n is the number of sides for
    each die.

    return the total sum of all these dice
    """
    total = 0
    for dice in range (number_of_dice):
        dice_roll = random.randint(1,n)
        total = dice_roll + total
    return total
