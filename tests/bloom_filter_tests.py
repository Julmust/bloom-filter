import pytest

from bloom_filter import BloomFilter


@pytest.fixture(scope='session')
def base_obj():
    bf = BloomFilter(10, 0.05)
    bf.insert('Hello, world!')
    return bf


def test_is_present_true(base_obj):
    assert base_obj.is_present('Hello, world!')


def test_is_present_false(base_obj):
    assert not base_obj.is_present('Hello, world')
