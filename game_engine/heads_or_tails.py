"""
Module: heads_or_tails.py
"""
import random

class HeadsOrTails:
    """
    Class: HeadsOrTails
    """
    def __init__(self, num_flips: int) -> None:
        self._heads = 0
        self._heads_counter = 0
        
        self._tails = 1
        self._tails_counter = 0

        self._num_flips = num_flips

    @property
    def heads(self) -> int:
        return self._heads

    @heads.setter
    def heads(self, heads: int) -> None:
        self._heads = heads

    @property
    def heads_counter(self) -> int:
        return self._heads_counter

    @heads_counter.setter
    def heads_counter(self, heads_counter: int) -> None:
        self._heads_counter = heads_counter

    @property
    def num_flips(self) -> int:
        return self._num_flips

    @num_flips.setter
    def num_flips(self, num_flips: int) -> None:
        self._num_flips = num_flips

    @property
    def tails(self) -> int:
        return self._tails

    @tails.setter
    def tails(self, tails: int) -> None:
        self._tails = tails

    @property
    def tails_counter(self) -> int:
        return self._tails_counter

    @tails_counter.setter
    def tails_conuter(self, tails_counter: int) -> None:
        self._tails_counter = tails_counter

    def flip(self) -> None:
        flips = random.choices([self.heads, self.tails], k = self.num_flips)
        
        self._heads_counter = flips.count(self.heads)
        self._tails_counter = self.num_flips - self.heads_counter

    def print_stats(self) -> None:
        heads_percentage = self.heads_counter / self.num_flips * 100
        tails_percentage = self.tails_counter / self.num_flips * 100

        print(f"Total Num Heads: {self.heads_counter:,}")
        print(f"Total Num Tails: {self.tails_counter:,}")
        print("")
        print(f"Percentage Of Heads: {heads_percentage:.2f}")
        print(f"Percentage Of Tails: {tails_percentage:.2f}")

