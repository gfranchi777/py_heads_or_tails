"""
Module: heads_or_tails.py
"""
import random
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

        self.flip()
        self.print_results()

    def get_formatted_flips_duration(self) -> str:
        if self._flips_duration < 1:
            formatted_duration = f"{self._flips_duration * 1000:.2f} Milliseconds"
        elif self._flips_duration < 60:
            formatted_duration = f"{self._flips_duration:.2f} Seconds"
        else:
            minutes = int(self._flips_duration // 60)
            seconds = int(self._flips_duration % 60)
            formatted_duration = f"{minutes:02d}:{seconds:02d} Minutes"
    
        return formatted_duration

    def flip(self) -> None:
        print(f"Flipping A Coin {self._num_flips:,} Times.\n")

        start_time = time.time()

        flips = random.choices([self._heads, self._tails], k = self._num_flips)
        
        end_time = time.time()

        self._flips_duration = end_time - start_time

        self._heads_counter = flips.count(self._heads)
        self._tails_counter = self._num_flips - self._heads_counter

        self._heads_percentage = round((self._heads_counter / self._num_flips) * 100, 5)
        self._tails_percentage = round((self._tails_counter / self._num_flips) * 100, 5)
    
    def is_valid_num_flips(self, num_flips: int) -> bool:
        try:
            self._num_flips = int(num_flips)
            
            if self._num_flips < 1:
                raise ValueError

            return True
        except ValueError:
            print(f"\nValue \"{num_flips}\" Is Not A Valid Number Of Flips.")
            return False

    def print_results(self) -> None:
        print(f"It Took {self.get_formatted_flips_duration()} To Run The {self._num_flips:,} Coin Flips.\n")
        
        print(f"Total Number Of Heads: {self._heads_counter:,}")
        print(f"Total Number Of Tails: {self._tails_counter:,}\n")
        
        print(f"Percentage Of Head Flips: {self._heads_percentage}%")
        print(f"Percentage Of Tail Flips: {self._tails_percentage}%")

