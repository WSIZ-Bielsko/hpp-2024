from hpp_2024.basics.user_repo import UserRepo


def test_user_repo():
    repo = UserRepo()
    assert repo


def test_can_create_user():
    repo = UserRepo()
    user = repo.create_user()
    assert user


def test_can_use_fixture(shared_secret):
    assert shared_secret


def test_can_use_fixture(user_repo):
    assert user_repo
