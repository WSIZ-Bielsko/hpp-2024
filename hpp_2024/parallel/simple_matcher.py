from difflib import SequenceMatcher


def are_almost_equal(a: str, b: str, min_match_percentage: float) -> bool:
    return SequenceMatcher(None, a, b).ratio() >= min_match_percentage
    # return sum(a_ == b_ for a_, b_ in zip(a, b)) / len(a) >= min_match_percentage


def test_simple1():
    assert are_almost_equal('A', 'A', 0.8)


def test_simple2():
    assert are_almost_equal('ABCD', 'ABCD', 0.8)


def test_simple3():
    assert are_almost_equal('AACCTTGG', 'AAACTTGG', 0.7)


def test_simple4():
    assert are_almost_equal('1234567890', '1234567---', 0.7)


if __name__ == '__main__':
    print(are_almost_equal('XXXXTTGG', 'AAACTTGG', 0.7))
