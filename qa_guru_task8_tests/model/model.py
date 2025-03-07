from selene import browser, have, command, by
from qa_guru_task8_tests.resources import path
from qa_guru_task8_tests.users import User


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_full_name(self, value):
        full_name = value.split()
        browser.element("#firstName").type(full_name[0])
        browser.element("#lastName").type(full_name[1])

    def fill_email(self, param):
        browser.element("#userEmail").type(param)

    def choose_gender(self, selector):
        browser.element(by.text(selector)).perform(command.js.click())

    def fill_phonenumber(self, number):
        browser.element("#userNumber").type(number)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(f'[value="{month-1}"]').click()
        browser.element(".react-datepicker__year-select").click().element(f'[value="{year}"]').click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def choose_subjects(self, subject):
        browser.element("#subjectsInput").click().type(subject).press_enter()

    def choose_hobbies(self, selectors):
        for hobbie in selectors:
            browser.element(by.text(hobbie)).click()

    def upload_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(path(file_name))

    def input_current_address(self, address):
        browser.element("#currentAddress").type(address)

    def scroll(self, destitation):
        browser.element(destitation).perform(command.js.scroll_into_view)

    def state_select(self, state):
        browser.element('#state').click().element(by.text(state)).click()

    def city_select(self, city):
        browser.element('#city').click().element(by.text(city)).click()

    def submit(self):
        browser.element("#submit").click()

    def filled_form_validation(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.all("//div[@class='table-responsive']//td[2]").should(
            have.exact_texts(user.full_name, user.email, user.gender, user.phone_number,
                             user.date_of_birth.strftime("%d %B,%Y"), user.subjects, ", ".join(user.hobbies),
                             user.picture,user.current_address, f"{user.state} {user.city}"))

    def registration(self, user: User):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phonenumber(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth.year, user.date_of_birth.month, user.date_of_birth.day)
        self.choose_subjects(user.subjects)
        self.choose_hobbies(user.hobbies)
        self.upload_picture(user.picture)
        self.input_current_address(user.current_address)
        self.scroll("#state")
        self.state_select(user.state)
        self.city_select(user.city)



