from datetime import date

from qa_guru_task8_tests.model.model import RegistrationPage
from qa_guru_task8_tests.users import User


def test_full_complited_form():
    student = User(full_name="Ivan Ivanovich", email="Ivanovich@testmail.com", gender="Male",
                   phone_number="7999999999", date_of_birth=date(2005, 5, 28), subjects="English",
                   hobbies=["Sports", "Reading"], picture="images.png", current_address="Test address, 11/1",
                   state="Haryana", city="Panipat")

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.registration(student)
    registration_page.submit()
    registration_page.filled_form_validation(student)