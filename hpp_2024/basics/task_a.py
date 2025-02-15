def solution_task_A(singural: str) -> str:
    pass


def test_zero():
    assert solution_task_A('myszkaus') == 'myszkai'


def test_empty():
    assert solution_task_A('us') == 'i'


def test_repeat():
    assert solution_task_A('ususus') == 'ususi'