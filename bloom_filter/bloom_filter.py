import mmh3

SEEDS = [42, 684, 9278]

def hash(val: str) -> int:
    return [mmh3.hash(val, i) % 1000 for i in SEEDS]


def main():
    ...


if __name__ == '__main__':
    main()
