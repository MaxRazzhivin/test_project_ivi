from pages.main_page import open_page, close_cookie, NotAuthorised, Authorised, return_to_main_page
import allure

from tests.conftest import email, password


from allure_commons.types import Severity




# @allure.tag("web")
# @allure.label("owner", "Max Razzhivin")
# @allure.feature("Здесь мы проверяем основные разделы главной страницы")
# @allure.story("При входе мы видим главные разделы сайта - 'Мой иви', 'Фильмы',"
#               " 'Сериалы', 'Мультфильмы'")
# @allure.link("https://www.ivi.ru/", "Ivi.ru main page")
# @allure.severity(Severity.CRITICAL)
# def test_main_page():
#     no_login=NotAuthorised()
#     with allure.step("Открываем главную страницу"):
#         open_page()
#     with allure.step("Закрываем нижнюю плашку про cookie"):
#         close_cookie()
#     with allure.step("Проверяем, что присутствуют основные разделы сайта"
#                      "Мой иви, Фильмы, Сериалы, Мультфильмы"):
#         no_login.main_sections_are_visible()


@allure.tag("web")
@allure.label("owner", "Max Razzhivin")
@allure.feature("Здесь проверяем основные разделы главной страницы - что по ним можно перейти")
@allure.story("При входе на главную страницу мы можем перейти на другие разделы сайта "
              "- 'Мой иви', 'Фильмы', 'Сериалы', 'Мультфильмы'")
@allure.link("https://www.ivi.ru/", "Ivi.ru main page")
@allure.severity(Severity.CRITICAL)
def test_links_of_main_directions():
    no_login=NotAuthorised()
    with allure.step("Открываем главную страницу"):
        open_page()
    with allure.step("Проверяем переходы по разделам - Мой иви, фильмы, сериалы и мультфильмы"):
        no_login.links_to_main_directions()





@allure.tag("web")
@allure.label("owner", "Max Razzhivin")
@allure.feature("Здесь мы проверяем авторизацию на сайте и выходим из аккаунта после проверки")
@allure.story("Мы можем авторизоваться на сайте и выйти из аккаунта")
@allure.link("https://www.ivi.ru/", "Ivi.ru")
@allure.severity(Severity.CRITICAL)
def test_authorisation():
    with allure.step("Открываем главную страницу"):
        main_page = Authorised()
        open_page()

    with allure.step("Авторизуемся как существующий пользователь через логин и пароль"):
        main_page.authorisation(email, password)

    with allure.step("Проверяем успешность авторизации, на аватарке отображается первая буква от email"):
        main_page.successful_login()

    with allure.step('Возвращаемся в главное меню'):
        return_to_main_page()

    with allure.step('Выходим из аккаунта'):
        main_page.logout()


@allure.tag("web")
@allure.label("owner", "Max Razzhivin")
@allure.feature("Проверяем поиск фильма и переходим в карточку")
@allure.story("Мы можем найти фильм через поиск и перейти в его карточку")
@allure.link("https://www.ivi.ru/", "Ivi.ru")
@allure.severity(Severity.CRITICAL)
def test_search_movie():
    with allure.step('Ищем кино, переходим на его страничку'):
        find_page = NotAuthorised()
        find_page.search_movie("Зимородок")

@allure.tag("web")
@allure.label("owner", "Max Razzhivin")
@allure.feature("Проверяем добавление в избранное")
@allure.story("Мы можем найти фильм и добавить в избранное")
@allure.link("https://www.ivi.ru/", "Ivi.ru")
@allure.severity(Severity.NORMAL)
def test_add_to_favourite():
    main_page = Authorised()
    find_page=NotAuthorised()
    with allure.step("Открываем главную страницу"):
        open_page()

    with allure.step("Авторизуемся как существующий пользователь через логин и пароль"):
        main_page.authorisation(email, password)

    with allure.step("Проверяем успешность авторизации, на аватарке отображается первая буква от email"):
        main_page.successful_login()

    with allure.step('Ищем кино, переходим на его страничку'):
        find_page.search_movie("Зимородок")

    with allure.step('Добавляем в избранное и проверяем результат, убираем из избранного, '
                     'выходим на главную страницу'):
        main_page.add_to_favourite("Зимородок")

    with allure.step('Выходим из аккаунта'):
        main_page.logout()


