import math
import random

import mmh3
import numpy as np


class BloomFilter:
    def __init__(self, exp_items: int, acc_false_pos_rate: float):
        no_bits = (-1 * exp_items) * np.log(acc_false_pos_rate) / pow(np.log(2), 2)
        no_hash_funcs = math.ceil(no_bits / (exp_items * np.log(2)))

        # FIXME: Possible to get two seeds with the same value
        self.seeds = [random.randint(1, (no_hash_funcs * 1000)) for i in range(no_hash_funcs)]
        self.arr = [0] * math.ceil(no_bits)

    def hash(self, val: str) -> list:
        """
        Consistently hash the incoming values with a seed
        """
        return [mmh3.hash(val, seed) % len(self.arr) for seed in self.seeds]

    def insert(self, val):
        """
        Insert value if it is not present.
        """
        hp = self.hash(val)

        # If the value _might_ be present, we don't have to edit the array
        if not self.is_present(val):
            for h in hp:
                self.arr[h] = 1

    def is_present(self, val) -> bool:
        """
        Check if a value might be present. With Bloom filters false positives
        are possible but not false negatives.
        """
        hp = self.hash(val)
        total = sum([self.arr[p] for p in hp])

        if total == len(self.seeds):
            return True

        return False


if __name__ == '__main__':
    bf = BloomFilter(10, 0.5)
