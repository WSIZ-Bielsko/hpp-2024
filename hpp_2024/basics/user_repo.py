from faker import Faker
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    pesel: str
    address: str


class UserRepo:
    def __init__(self):
        self.faker = Faker('pl_PL')

    def create_user(self) -> User:
        pass


if __name__ == '__main__':
    repo = UserRepo()
    print(repo.faker.first_name())
    print(repo.faker.last_name())
    print(repo.faker.pesel())
    print(repo.faker.address())
