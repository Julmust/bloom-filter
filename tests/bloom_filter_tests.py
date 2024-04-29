from bloom_filter import hash


def test_hashing():
    res = hash('Hello, world!')
    assert res == [643, 403, 247]