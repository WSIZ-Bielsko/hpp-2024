import pytest

from hpp_2024.basics.user_repo import UserRepo


@pytest.fixture
def shared_secret():
    return "sEcReT"


@pytest.fixture
def user_repo():
    repo = UserRepo()
    return repo


@pytest.fixture
def user(user_repo):
    return user_repo.create_user()