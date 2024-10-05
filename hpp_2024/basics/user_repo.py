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


class UserRepo:
    def __init__(self):
        self.faker = Faker('pl_PL')

    def create_user(self) -> User:
        name = self.faker.first_name()
        surname = self.faker.last_name()
        age = self.faker.random_int(0, 100)
        pesel = self.faker.pesel()
        address = self.faker.address()
        return User(name=name, surname=surname, age=age, pesel=pesel, address=address)

