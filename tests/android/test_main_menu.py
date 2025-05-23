import allure
from pages.android import main_menu
from tests.android.conftest import email, password


@allure.title('Control buttons should be visible')
@allure.epic('Bottom menu')
@allure.story('Bottom menu')
@allure.feature('Control buttons in bottom menu')
@allure.label('microservice', 'Bottom menu')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_control_buttons_should_be_visible():

    main_menu.close_advertisement()

    main_menu.button_my_ivi_should_be_visible()
    main_menu.button_search_should_be_visible()
    main_menu.button_stream_should_be_visible()
    main_menu.button_favourite_should_be_visible()
    main_menu.button_profile_should_be_visible()





@allure.title('Search function testing')
@allure.epic('Bottom menu')
@allure.story('Bottom menu')
@allure.feature('Search function and verify result')
@allure.label('microservice', 'Search func')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_search():
    main_menu.close_advertisement()

    main_menu.search_function_and_verify_result('Батя')



@allure.title('Profile authorization')
@allure.epic('Bottom menu')
@allure.story('Bottom menu')
@allure.feature('Test of authorization of user')
@allure.label('microservice', 'Authorization')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_authorization():

    main_menu.close_advertisement()

    main_menu.profile_page(email, password)