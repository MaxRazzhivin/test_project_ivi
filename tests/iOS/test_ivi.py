import allure

from pages.iOS import main_page
from tests.iOS.conftest import email, password


@allure.title('Control buttons should be visible and active')
@allure.epic('Bottom and header menu')
@allure.story('Bottom and header menu')
@allure.feature('Control buttons in bottom and header menu')
@allure.label('microservice', 'Bottom and header menu')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_control_buttons_should_be_visible():

    main_page.close_advertisement()
    main_page.button_my_ivi_should_be_visible()
    main_page.button_search_should_be_visible()
    main_page.button_stream_should_be_visible()
    main_page.button_favourite_should_be_visible()
    main_page.button_profile_should_be_visible()

    main_page.buttons_of_header_section_are_clickable()





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
    main_page.close_advertisement()
    main_page.search_function_and_verify_result('Достать ножи')



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

    main_page.close_advertisement()
    main_page.profile_page(email, password)