from difflib import SequenceMatcher


def are_quasi_equal(a: str, b: str, min_match_percentage: float) -> bool:
    ratio = SequenceMatcher(lambda x: x in 'N', a, b).ratio()
    print(f'{ratio=}')
    return ratio >= min_match_percentage
    # return sum(a_ == b_ for a_, b_ in zip(a, b)) / len(a) >= min_match_percentage


def test_simple1():
    assert are_quasi_equal('ANA', 'AAA', 0.8)


def test_simple2():
    assert are_quasi_equal('T', 'N', 0.8)


def test_simple3():
    assert are_quasi_equal('NNNNABCD', 'XXXXABCD', 0.7)


def test_simple4():
    assert are_quasi_equal('1234567890', '1234567---', 0.7)

def test_simple5():
    assert are_quasi_equal('1234567890', '1234567NNN', 1.0)


if __name__ == '__main__':
    print(are_quasi_equal('XXXXTTGG', 'AAACTTGG', 0.7))
