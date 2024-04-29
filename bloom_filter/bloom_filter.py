import mmh3


class BloomFilter:
    def __init__(self):
        self.seeds =  [42, 684, 9278]
        self.arr = [0] * 1000

    def hash(self, val: str) -> list:
        return [mmh3.hash(val, seed) % 1000 for seed in self.seeds]

    def insert(self, val):
        hp = self.hash(val)

        # If the value _might_ be present, we don't have to edit the array
        if not self.is_present(val):
            for h in hp:
                self.arr[h] = 1


    def is_present(self, val) -> bool:
        hp = self.hash(val)
        total = sum([self.arr[p] for p in hp])

        if total == 3:
            return True

        return False

