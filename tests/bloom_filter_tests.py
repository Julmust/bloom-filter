import pytest

from bloom_filter import BloomFilter


@pytest.fixture(scope='session')
def base_obj():
    bf = BloomFilter()
    bf.insert('Hello, world!')
    return bf

def test_hashing(base_obj):
    res = base_obj.hash('Hello, world!')

    assert res == [643, 403, 247]


def test_insert(base_obj):
    for v in [643, 403, 247]:
        assert base_obj.arr[v] == 1


def test_is_present_true(base_obj):
    assert base_obj.is_present('Hello, world!')


def test_is_present_false(base_obj):
    assert not base_obj.is_present('Hello, world')
