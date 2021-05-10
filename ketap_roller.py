#!/usr/bin/env python3
from random import randint
import sys
import re

MIN_ROLL = 1
MIN_DICE = 1
MIN_SIDES = 2
DEFAULT_MOD = 0
results = list()
args = sys.argv[1:]

def roll_dice(dice_num=MIN_DICE, dice_sides=20, mod=DEFAULT_MOD):
    if (dice_num < MIN_DICE) or (dice_sides <= MIN_SIDES):
       size_err_msg = f'''
       dice_num must be
       {MIN_DICE} or greater and dice_sides must be
       {MIN_SIDES} or greater, mod must be 0 or greater'''
       print(size_err_msg)
       raise ValueError
    else:
        i = 0
        while i < dice_num:

            yield randint(MIN_ROLL, dice_sides) + mod
            i += 1

def parse_args(input_arr):
    i = 0
    while i < len(input_arr):
        try:

            dice_num_regex = r'^\d+d'
            input_dice_num = re.search(dice_num_regex, input_arr[i]).group()
            input_dice_num = input_dice_num.replace("d", "")

            dice_side_regex = r'd\d+\s*'
            input_dice_sides = re.search(dice_side_regex, input_arr[i]).group()
            input_dice_sides = input_dice_sides.replace("d","")

            dice_mod_pos_regex = r'\+\d+$'
            dice_mod_neg_regex = r'-\d+$'

            pos_match = re.search(dice_mod_pos_regex, input_arr[i])
            neg_match = re.search(dice_mod_neg_regex, input_arr[i])

            if pos_match != None:

                pos_match = pos_match.group().replace("+", "")
                input_dice_mod = pos_match


            elif neg_match != None:
                neg_match = neg_match.group()
                input_dice_mod = neg_match

            else:
                input_dice_mod = "0"

            input_dice_num = int(input_dice_num)
            input_dice_sides = int(input_dice_sides)
            input_dice_mod = int(input_dice_mod)

        except ValueError or AttributeError:
            print ("Failed to parse dice info")
            sys.exit(1)

        yield (input_dice_num, input_dice_sides, input_dice_mod)
        i += 1

def play(input):

    for i in parse_args(input):
        for j in roll_dice(i[0], i[1], i[2]):
            if i[2] >= 0:
                print(f"Result of {i[0]}d{i[1]}+{i[2]} is: {j}")
            elif i[2] < 0:
                print(f"Result of {i[0]}d{i[1]}{i[2]} is: {j}")

play(args)
