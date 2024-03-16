"""
Module: heads_or_tails.py
"""
import random
import sys

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
        self.print_stats()

    @property
    def heads_counter(self) -> int:
        return self._heads_counter

    @property
    def num_flips(self) -> int:
        return self._num_flips

    @property
    def tails_counter(self) -> int:
        return self._tails_counter

    def flip(self) -> None:
        print(f"\nFlipping A Coin {self.num_flips:,} Times.\n")

        flips = random.choices([self._heads, self._tails], k = self._num_flips)
        
        self._heads_counter = flips.count(self._heads)
        self._tails_counter = self._num_flips - self._heads_counter

    def is_valid_num_flips(self, num_flips: int) -> bool:
        try:
            self._num_flips = int(num_flips)
            
            if self.num_flips < 1:
                raise ValueError

            return True
        except ValueError:
            print(f"\nValue \"{num_flips}\" Is Not A Valid Number Of Flips.")
            return False

    def print_stats(self) -> None:
        heads_percentage = self._heads_counter / self._num_flips * 100
        tails_percentage = self._tails_counter / self._num_flips * 100

        print(f"Total Num Heads: {self._heads_counter:,}")
        print(f"Total Num Tails: {self._tails_counter:,}")
        print("")
        print(f"Percentage Of Heads: {heads_percentage:.2f}")
        print(f"Percentage Of Tails: {tails_percentage:.2f}")

