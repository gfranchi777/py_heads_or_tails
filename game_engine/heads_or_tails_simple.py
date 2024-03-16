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
        # Make sure that the num_flips are a valid integer value greater than 0
        try:
            num_flips = int(num_flips)

            if num_flips < 1:
                raise ValueError

            heads = 0
            tails = 1
        except ValueError:
            print(f"\nValue \"{num_flips}\" Is Not A Valid Number Of Flips.")
            sys.exit(1)

        # Perform the coin flips
        flips = random.choices([heads, tails], k = num_flips)
        
        # Populate the statistic variables
        heads_counter = flips.count(heads)
        tails_counter = num_flips - heads_counter

        heads_percentage = heads_counter / num_flips * 100
        tails_percentage = tails_counter / num_flips * 100

        # Print the results to the console
        print("")
        print(f"Flipping A Coin {heads_or_tails.num_flips:,} Times.")
        print("")
        print(f"Total Num Heads: {heads_counter:,}")
        print(f"Total Num Tails: {tails_counter:,}")
        print("")
        print(f"Percentage Of Heads: {heads_percentage:.2f}")
        print(f"Percentage Of Tails: {tails_percentage:.2f}")

