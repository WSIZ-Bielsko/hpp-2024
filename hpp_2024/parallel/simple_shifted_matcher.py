from difflib import SequenceMatcher


def are_quasi_shifted_equal(a: str, b: str, min_match_percentage: float, max_shift: int) -> bool:
    return SequenceMatcher(None, a, b).ratio() >= min_match_percentage
    # return sum(a_ == b_ for a_, b_ in zip(a, b)) / len(a) >= min_match_percentage


def test_simple1():
    assert are_quasi_shifted_equal('AAABBB', 'BBBAAA', 0.99, max_shift=3)
    # from a: 'BBB'; from b: 'BBB'


def test_simple2():
    assert are_quasi_shifted_equal('AAACTGCTG', 'ACTGCTGNN', 0.8, max_shift=2)
    # 'ACTGCTG' is substring of both: a and b

def test_simple3():
    assert are_quasi_shifted_equal('AAGCTGCTG', 'ACTGCTGNN', 0.7, max_shift=2)

def test_simple4():
    assert are_quasi_shifted_equal('SSAAAXAAA', 'AAAYAAASS', 0.99, max_shift=2)
    # can cut out the substring AAAXAAA from a, and AAAYAAA from b




if __name__ == '__main__':
    print(are_quasi_shifted_equal('XXXXTTGG', 'AAACTTGG', 0.7))
