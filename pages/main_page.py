from selene.support.shared import browser
from selene import have, by, be
from tests.conftest import email


def open_page():
    browser.open('/')


def close_cookie():
    # Закрываем мешающее сообщение про куки
    browser.element('[data-test="accept-teaser-button"]').click()


def return_to_main_page():

    # Возврат в главное меню

    browser.element('[data-test="header_logo"]').click()


class Authorised:

    def free_subscribe_button(self):

        # Проверяем путь существующего пользователя в режиме инкогнито - должно открыться окно с рекламным баннером
        # и кнопкой "Попробовать 30 дней бесплатно"

        browser.element('.segmentedLanding__section_main .nbl-button__primaryText').should(
            have.text('Попробовать 30 дней бесплатно')).click()

    def authorisation(self, login, password):

        # Находим кнопку для авторизации, нажимаем, вводим логин

        browser.element('[data-test="header_avatar"]').click()
        browser.element('[data-testid="profile_main_page"] .nbl-button_style_kioshi').click()
        # browser.element('[data-test="navbar_title"]').should(have.text('Вход или регистрация'))
        # browser.element('.nbl-input__placeholder').should(have.text('Введи email или телефон'))
        browser.element('[data-test="input_login"]').type(login).press_enter()

        # Вводим пароль и нажимаем enter
        # browser.element('[data-testid="nextMethodButton"]').click()

        browser.element('[data-test="input_password"]').type(password).press_enter()

        # Проверяем успешность авторизации - наличие надписи "успешный вход"

        browser.element('[data-fixed="true"] .nbl-chatMessage__title').should(have.text('Успешный вход'))

    def successful_login(self):

        # Проверяем, что авторизация прошла успешно, отображается аватарка, на ней заглавная первая буква
        # от нашего email
        first_letter = email[0].upper()  # Получаем первую букву email в верхнем регистре
        browser.element('[data-testid="profile_main_page"] .nbl-avatar__text').should(be.visible).should(
            have.text(first_letter))

    def add_to_favourite(self, value):

        # Поиск фильма и переход на его страницу, добавление в список "буду смотреть"
        # и проверка, что добавлен - затем убираем из списка и выходим на главное меню

        # Добавляем фильм в избранное (список "буду смотреть")
        browser.element('[data-test="favorite_button"]').click()

        # Заходим на личную страницу профиля - проверяем, что фильм добавился к нам
        browser.element('.nbl-avatar__text').should(be.visible).click()

        # Заходим в список "буду смотреть" внутри личного кабинета
        browser.element('.profileMenu__list_tile .profileMenu__item:nth-child(4)').click()

        # Проверяем, что фильм присутствует в списке и добавлен корректно
        (browser.element('.profileGallery .gallerySection__list > li:nth-child(1)').should
         (have.exact_text(value)).click())

        # Убираем его из списка избранного "буду смотреть"
        browser.element('[data-test="favorite_button"]').click()

        # Возвращаемся на главную страницу
        return_to_main_page()

    def logout(self):

        # Заходим в меню пользователя и далее выход из аккаунта

        browser.element('.nbl-avatar__text').should(be.visible).click()
        browser.element('.profileMain__footer').element(by.text("Выйти")).click()
        browser.element('.confirmLogout').element(by.text("Выйти")).click()


class NotAuthorised:
    def main_sections_are_visible(self):
        browser.element('#headerTop').should(have.text('Мой Иви'))
        browser.element('#headerTop').should(have.text('Фильмы'))
        browser.element('#headerTop').should(have.text('Сериалы'))
        browser.element('#headerTop').should(have.text('Мультфильмы'))

    def links_to_main_directions(self):

        # Переходим на вкладку "Мой иви"
        browser.element('[data-test="menu_section_my_ivi"]').click()

        # Закрываем popup окно, если оно отображается

        # if browser.element('[data-test="promoBlock"]').should(be.visible):
        browser.element('.fullscreen-popup__scroll-wrapper .nbl-controlButton__caption').click()
        # else:
        #     pass

        # Переходим на вкладку "Фильмы"

        browser.element('[data-test="menu_section_films"]').click()

        # Переходим на вкладку "Сериалы"

        browser.element('[data-test="menu_section_menu_serials"]').click()

        # Переходим на вкладку "Мультфильмы"

        browser.element('[data-test="menu_section_kids"]').click()

        # Возвращаемся на главное меню

        return_to_main_page()

    def search_movie(self, value):

        open_page()

        # Нажимаем на инпут "Поиск"
        browser.element('[data-test="header_search"]').click()

        # Вводим название фильма (для тех, которые есть на ivi.ru) и переходим на страницу кино
        browser.element('[data-test="search_input"]').type(value)

        browser.element('.searchResultItem').click()
