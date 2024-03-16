"""
Module: heads_or_tails.py
"""
import numpy as np
import sys
import time

class HeadsOrTails:
    """
    Class: HeadsOrTails
    """
    def __init__(self, num_flips: int) -> None:
        if not self.is_valid_num_flips(num_flips):
            sys.exit(1)

        self._heads = 0
        self._heads_counter = 0
        
        self._tails = 1
        self._tails_counter = 0

        print(f"Flipping A Coin {self._num_flips:,} Times.\n")

        # Flip the coin and determine the sum duration of the flips
        start_time = time.time()
        self.flip()
        end_time = time.time()
        self._flips_duration = self.get_formatted_time(end_time - start_time)

        # Calculate the stats of the coin flips and determine the duration of the calculation
        start_time = time.time()
        self.calculate_stats()
        end_time = time.time()
        self._calculate_stats_duration = self.get_formatted_time(end_time - start_time)
        
        self.print_results()

    def calculate_stats(self) -> None:
        """
        Function: calculate_stats
        """
        self._heads_counter = np.sum(self._flips == 0)
        self._tails_counter = self._num_flips - self._heads_counter

        self._heads_percentage = round((self._heads_counter / self._num_flips) * 100, 5)
        self._tails_percentage = round((self._tails_counter / self._num_flips) * 100, 5)
    
    def get_formatted_time(self, unformatted_time: float) -> str:
        """
        Function: get_formatted_flips_duration
        """
        if unformatted_time < 1:
            formatted_time = f"{unformatted_time * 1000:.2f} Milliseconds"
        elif unformatted_time < 60:
            formatted_time = f"{unformatted_time:.2f} Seconds"
        else:
            minutes = int(unformatted_time // 60)
            seconds = int(unformatted_time % 60)
            formatted_time = f"{minutes:02d}:{seconds:02d} Minutes"
    
        return formatted_time

    def flip(self) -> None:
        """
        Function: flip
        """
        self._flips = np.random.randint(2, size = self._num_flips)

    def is_valid_num_flips(self, num_flips: int) -> bool:
        """
        Function: is_valid_num_flips
        """
        try:
            self._num_flips = int(num_flips)
            
            if self._num_flips < 1:
                raise ValueError

            return True
        except ValueError:
            print(f"\nValue \"{num_flips}\" Is Not A Valid Number Of Flips.")
            return False

    def print_results(self) -> None:
        """
        Function: print_results
        """
        print(f"It Took {self._flips_duration} To Run The {self._num_flips:,} Coin Flips.\n")
        
        print(f"Total Number Of Heads: {self._heads_counter:,}")
        print(f"Total Number Of Tails: {self._tails_counter:,}\n")

        print(f"Percentage Of Head Flips: {self._heads_percentage}%")
        print(f"Percentage Of Tail Flips: {self._tails_percentage}%\n")

        print(f"It Took {self._calculate_stats_duration} To Run The calculate_stats Function.\n")

