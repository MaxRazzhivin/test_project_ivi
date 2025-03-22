import os
from selene.support.shared import browser
from selene import have, by, be, command

from tests.conftest import email


class OpenMainPage:
    def open(self):
        browser.open('https://www.ivi.ru/')

        # # Удаляем рекламу
        # browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        # browser.driver.execute_script("$('#fixedban').remove()")
        # browser.driver.execute_script("$('footer').remove()")

    # def scroll_page(self):
    #     browser.execute_script('window.scrollBy(0, 400);')
    #     return self

    def free_subscribe_button(self):

        # Проверяем путь существующего пользователя в режиме инкогнито - должно открыться окно с рекламным баннером
        # и кнопкой "Попробовать 30 дней бесплатно"

        browser.element('.segmentedLanding__section_main .nbl-button__primaryText').should(
            have.text('Попробовать 30 дней бесплатно')).click()

    def authorisation(self, login, password):

        # Проверяем наличие надписи "Вход или регистрация" и вводим почту, жмем далее

        browser.element('[data-test="navbar_title"]').should(have.text('Вход или регистрация'))
        browser.element('.nbl-input__placeholder').should(have.text('Введи email или телефон'))
        browser.element('[data-test="input_login"]').type(login)
        browser.element('[data-test="button_continue"]').click()

        # Вводим пароль и нажимаем enter

        browser.element('.nbl-chatMessage__extraItem').should(
            have.text('Введи пароль аккаунта Иви'))
        browser.element('[data-test="input_password"]').type(password).press_enter()

        # Проверяем успешность авторизации - наличие надписи "успешный вход"

        browser.element('[data-fixed="true"] .nbl-chatMessage__title').should(have.text('Успешный вход'))

        # Проверяем надпись на кнопке "Не интересует" и жмем на нее
        browser.element('[data-test="not_interested_button"]').should(have.text('Не интересует')).click()

        # Выходим в главное меню после авторизации по кнопке "Назад"

        browser.element('.segmentedLanding__section_main .nbl-controlButton__caption').should(have.text('Назад')).click()

    def successful_login(self):

        # Проверяем, что авторизация прошла успешно, отображается аватарка и переходим в меню пользователя
        browser.element('.nbl-avatar__text').should(be.visible).click()

    def profile_menu(self):

        # Проверяем, что авторизация прошла успешно, на аватарке заглавная первая буква от нашего email

        first_letter = email[0].upper()  # Получаем первую букву email в верхнем регистре
        browser.element('[data-testid="profile_main_page"] .nbl-avatar__text').should(be.visible).should(
            have.text(first_letter))

    def return_to_main_page(self):

        # Возврат в главное меню

        browser.element('[data-test="header_logo"]').click()

    def logout(self):

        # Заходим в меню пользователя и далее выход из аккаунта

        OpenMainPage.successful_login(self)
        browser.element('.profileMain__footer').element(by.text("Выйти")).click()
        browser.element('.confirmLogout').element(by.text("Выйти")).click()














    # def fill_first_name(self):
    #     browser.element('.segmentedLanding__section_main + .segmentedLanding__sticky_visible').click()
    #
    # def fill_last_name(self, value):
    #     browser.element('#lastName').type(value)
    #
    # def fill_email(self, value):
    #     browser.element('#userEmail').type(value)
    #
    # def fill_gender(self, value):
    #     browser.all('[name=gender]').element_by(have.value(value)).element("..").click()
    #
    # def fill_user_number(self, value):
    #     browser.element('#userNumber').type(value)
    #
    # def fill_date_of_birth(self, year, month, day):
    #     browser.element('#dateOfBirthInput').click()
    #     browser.element('.react-datepicker__month-select').type(month)
    #     browser.element('.react-datepicker__year-select').type(year)
    #     browser.element(f'.react-datepicker__day--0{day}').click()
    #
    # def fill_subjects(self, value):
    #     browser.element('#subjectsInput').type(value).press_tab()
    #
    # def fill_hobbies(self, value1, value2):
    #     browser.all('.custom-checkbox').element_by(have.exact_text(value1)).click()
    #     browser.all('.custom-checkbox').element_by(have.exact_text(value2)).click()
    #
    # def fill_image(self, path):
    #     browser.element("#uploadPicture").send_keys(
    #         os.path.abspath(os.path.join(os.path.dirname(__file__), f"../resources/{path}")))
    #
    # def fill_address(self, value):
    #     browser.element('#currentAddress').click().type(value)
    #
    # def fill_state(self, value):
    #     browser.element('#state').click().element(by.text(value)).click()
    #
    # def fill_city(self, value):
    #     browser.element('#city').click().element(by.text(value)).click()
    #
    # def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subject, hobbies, image_name, address,
    #                                 state_city):
    #     browser.element(".table").all('td').even.should(
    #         have.exact_texts(
    #             full_name,
    #             email,
    #             gender,
    #             mobile,
    #             date_of_birth,
    #             subject,
    #             hobbies,
    #             image_name,
    #             address,
    #             state_city,
    #     ))
    #
    # def button_close_should_be_clickable(self):
    #     browser.element('#closeLargeModal').should(be.clickable)
    #
    # def submit(self):
    #     browser.element('#submit').perform(command.js.click)
