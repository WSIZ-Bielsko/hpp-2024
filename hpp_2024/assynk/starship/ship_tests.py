import pytest

from hpp_2024.assynk.starship.model import Ship, add


@pytest.fixture
async def ship():
    return Ship()


@pytest.mark.asyncio
async def test_can_add(ship):
    res = await add(1, 2)
    assert res == 3


def test_bla_bla():
    x = 1
    y = 15
    z = x + y
    assert z == 16
