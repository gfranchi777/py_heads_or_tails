"""
Module: heads_or_tails_simple.py
"""
import random
import sys

class HeadsOrTailsSimple:
    """
    Class: HeadsOrTailsSimple
    """
    def __init__(self, num_flips: int) -> None:
        try:
            num_flips = int(num_flips)

            if num_flips < 1:
                raise ValueError
        except ValueError:
            print(f"\nValue \"{num_flips}\" Is Not A Valid Number Of Flips.")
            sys.exit(1)

        heads = 0
        tails = 1

        print(f"\nFlipping A Coin {num_flips:,} Times.\n")

        flips = random.choices([heads, tails], k = num_flips)
        
        heads_counter = flips.count(heads)
        tails_counter = num_flips - heads_counter

        heads_percentage = heads_counter / num_flips * 100
        tails_percentage = tails_counter / num_flips * 100

        print(f"Total Num Heads: {heads_counter:,}")
        print(f"Total Num Tails: {tails_counter:,}")
        print("")
        print(f"Percentage Of Heads: {heads_percentage:.2f}")
        print(f"Percentage Of Tails: {tails_percentage:.2f}")

