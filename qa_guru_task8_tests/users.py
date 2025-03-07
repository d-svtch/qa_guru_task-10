import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: date
    subjects: str
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str
