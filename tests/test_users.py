import pytest
from pydantic import ValidationError

from hpp_2024.basics.user_repo import UserRepo


def test_user_repo():
    repo = UserRepo()
    assert repo


def test_can_create_user():
    repo = UserRepo()
    user = repo.create_random_user()
    assert user


def test_can_use_fixture(shared_secret):
    assert shared_secret


def test_can_use_fixture(user_repo):
    assert user_repo


def test_users_are_frozen(user_repo):
    u = user_repo.create_random_user()
    with pytest.raises(ValidationError):
        u.name = 'Kadabra'


def test_users(user):
    assert len(user.name) >= 3
