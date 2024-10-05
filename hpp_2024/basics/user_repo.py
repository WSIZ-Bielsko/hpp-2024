from faker import Faker
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    pesel: str
    address: str

    class Config:
        frozen = True

"""
Prompt to generate UserRepo class methods for CRUD operations

given the following structure (users are stored in self.users, which is a dict from user.pesel -> 
reference to User instance); write methods for CRUD operations, in UserRepo class

(insert User and constructor of UserRepo class here)

"""


class UserRepo:
    def __init__(self):
        self.faker = Faker('pl_PL')
        self.users: dict[str, User] = {}

    def create_random_user(self) -> User:
        name = self.faker.first_name()
        surname = self.faker.last_name()
        age = self.faker.random_int(0, 100)
        pesel = self.faker.pesel()
        address = self.faker.address()
        return User(name=name, surname=surname, age=age, pesel=pesel, address=address)

    def create(self, user: User) -> User:
        if user.pesel in self.users:
            raise ValueError(f"User with PESEL {user.pesel} already exists")
        self.users[user.pesel] = user
        return user

    def read(self, pesel: str) -> User:
        user = self.users.get(pesel)
        if not user:
            raise ValueError(f"User with PESEL {pesel} not found")
        return user

    def update(self, pesel: str, updated_user: User) -> User:
        if pesel not in self.users:
            raise ValueError(f"User with PESEL {pesel} not found")
        if pesel != updated_user.pesel:
            raise ValueError("Cannot change PESEL")
        self.users[pesel] = updated_user
        return updated_user

    def delete(self, pesel: str) -> None:
        if pesel not in self.users:
            raise ValueError(f"User with PESEL {pesel} not found")
        del self.users[pesel]

    def list_all(self) -> list[User]:
        return list(self.users.values())
