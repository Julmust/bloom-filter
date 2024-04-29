import mmh3


class BloomFilter:
    def __init__(self):
        self.seeds = [42, 684, 9278]
        self.arr = [0] * 1000

    def hash(self, val: str) -> list:
        """
        Consistently hash the incoming values with a seed
        """
        return [mmh3.hash(val, seed) % 1000 for seed in self.seeds]

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

        if total == 3:
            return True

        return False
