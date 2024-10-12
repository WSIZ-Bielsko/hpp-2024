import random
from collections import Counter

import pytest

from hpp_2024.parallel.dna_tools import generate_random_dna


def test_dna_0():
    seq = generate_random_dna(n_elems=10)
    assert len(seq) == 10


def test_dna_1():
    random.seed(42)
    dna1 = generate_random_dna(100)
    random.seed(42)
    dna2 = generate_random_dna(100)
    assert dna1 == dna2


def test_dna_2():
    # fixme: this _is not guaranteed to succeed across all platforms and python versions
    random.seed(42)
    dna1 = generate_random_dna(20)
    expected = 'AAGCCCAATAAACCACTCTG'
    assert dna1 == expected


def test_generate_random_dna_3():
    with pytest.raises(TypeError):
        generate_random_dna("kip kip")


def test_all_tokens_used():
    tokens = ['A', 'C', 'G', 'T']
    dna = generate_random_dna(n_elems=1000)
    assert set(dna) == set(tokens)

def test_uniform_distribution():
    dna = generate_random_dna(10000)
    counts = Counter(dna)
    expected_count = 10000 / 4
    tolerance = expected_count * 0.05

    for nucleotide in ['A', 'T', 'C', 'G']:
        assert abs(counts[nucleotide] - expected_count) <= tolerance, f"Count for {nucleotide} is not within expected range"