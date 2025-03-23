import os
from selene.support.shared import browser
from selene import have, by, be, command
from tests.conftest import email


class IviPage:
    def open(self):
        browser.open('https://www.ivi.ru/')

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



    def search_movie(self, value):

        # Поиск фильма и переход на его страницу, добавление в список "буду смотреть"
        # и проверка, что добавлен - затем убираем из списка и выходим на главное меню

        # Нажимаем на инпут "Поиск"
        browser.element('[data-test="header_search"]').click()

        # Вводим название фильма (для тех, которые есть на ivi.ru) и переходим на страницу кино
        browser.element('[data-test="search_input"]').type(value)
        browser.element('.searchResultItem').click()

        # Добавляем фильм в избранное (список "буду смотреть")
        browser.element('[data-test="favorite_button"]').click()

        # Заходим на личную страницу профиля - проверяем, что фильм добавился к нам
        IviPage.successful_login(self)

        # Заходим в список "буду смотреть" внутри личного кабинета
        browser.element('.profileMenu__list_tile .profileMenu__item:nth-child(4)').click()

        # Проверяем, что фильм присутствует в списке и добавлен корректно
        browser.element('.profileGallery .gallerySection__list > li:nth-child(1)').should(have.exact_text(value)).click()

        # Убираем его из списка избранного "буду смотреть"
        browser.element('[data-test="favorite_button"]').click()

        # Возвращаемся на главную страницу
        IviPage.return_to_main_page(self)


    def logout(self):

        # Заходим в меню пользователя и далее выход из аккаунта

        IviPage.successful_login(self)
        browser.element('.profileMain__footer').element(by.text("Выйти")).click()
        browser.element('.confirmLogout').element(by.text("Выйти")).click()