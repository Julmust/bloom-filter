from bloom_filter import BloomFilter


def test_hashing():
    bf = BloomFilter()
    res = bf.hash('Hello, world!')

    assert res == [643, 403, 247]

def test_insert():
    bf = BloomFilter()
    bf.insert('Hello, world!')

    for v in [643, 403, 247]:
        assert bf.arr[v] == 1

def test_is_present_true():
    bf = BloomFilter()
    bf.insert('Hello, world!')

    assert bf.is_present('Hello, world!')

def test_is_present_false():
    bf = BloomFilter()
    bf.insert('Hello, world!')

    assert not bf.is_present('Hello, world')