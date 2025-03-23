from selene.support.shared import browser

from pages.main_page import IviPage
import allure

from tests.conftest import email, password


# from allure_commons.types import Severity


# @allure.tag("web")
# @allure.label("owner", "Max Razzhivin")
# @allure.feature("Проверяем тестовый функционал главной страницы")
# @allure.story("Пользователь может зайти авторизоваться")
# @allure.link("https://www.ivi.ru/", "Ivi.ru main page")
# @allure.severity(Severity.CRITICAL)
def test_ivi():
    with allure.step("Открываем главную страницу"):
        main_page = IviPage()
        main_page.open()

    with allure.step("Проверяем кнопку для подписки на 30 дней, что ее видно с корректным текстом и жмем на нее"):
        main_page.free_subscribe_button()

    with allure.step("Авторизуемся как существующий пользователь через логин и пароль"):
        main_page.authorisation(email, password)

    with allure.step("Проверяем успешность авторизации"):
        main_page.successful_login()

    with allure.step('Проверяем личный кабинет - на аватарке отображается первая буква от email'):
        main_page.profile_menu()

    with allure.step('Возвращаемся в главное меню'):
        main_page.return_to_main_page()

    with allure.step('Ищем кино, переходим на его страничку, проверяем добавление в избранное'):
        main_page.search_movie("Пчеловод")

    with allure.step('Выходим из аккаунта'):
        main_page.logout()