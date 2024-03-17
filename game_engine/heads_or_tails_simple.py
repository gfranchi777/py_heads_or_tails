"""
Module: heads_or_tails_simple.py
"""
import numpy as np
import sys
import time

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

        print(f"Flipping A Coin {num_flips:,} Times.\n")
        
        # Perform the coin flips and get the duration time of the flips
        start_time = time.time()
        
        flips = np.random.randint(2, size = num_flips)
        
        end_time = time.time()

        flips_duration = end_time - start_time
        
        # Populate the statistic variables and get the calculation duration time
        start_time = time.time()
        
        heads_counter = np.sum(flips == 0)
        
        tails_counter = num_flips - heads_counter

        heads_percentage = round((heads_counter / num_flips) * 100, 5)
        
        tails_percentage = round((tails_counter / num_flips) * 100, 5)

        end_time = time.time()

        calculate_stats_duration = end_time - start_time

        # Format the flips duration time
        if flips_duration < 1:
            formatted_flips_duration = f"{flips_duration * 1000:.2f} Milliseconds"
        elif flips_duration < 60:
            formatted_flips_duration = f"{flips_duration:.2f} Seconds"
        else:
            minutes = int(flips_duration // 60)
            seconds = int(flips_duration % 60)
            formatted_flips_duration = f"{minutes:02d}:{seconds:02d} Minutes"

        # Format the calculate stats duration
        if calculate_stats_duration < 1:
            formatted_calculate_stats_duration = f"{flips_duration * 1000:.2f} Milliseconds"
        elif calculate_stats_duration < 60:
            formatted_calculate_stats_duration = f"{flips_duration:.2f} Seconds"
        else:
            minutes = int(calculate_stats_duration // 60)
            seconds = int(calculate_stats_duration % 60)
            formatted_calculate_stats_duration = f"{minutes:02d}:{seconds:02d} Minutes"
        
        # Print the results to the console
        print(f"It Took {formatted_flips_duration} To Run The {num_flips:,} Coin Flips.\n")
        
        print(f"Total Number Of Heads: {heads_counter:,}")
        print(f"Total Number Of Tails: {tails_counter:,}\n")
        
        print(f"Percentage Of Head Flips: {heads_percentage}%")
        print(f"Percentage Of Tail Flips: {tails_percentage}%\n")

        print(f"It Took {formatted_calculate_stats_duration} To Calculate The Statisticsn.\n")

