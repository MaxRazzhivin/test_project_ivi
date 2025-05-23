"""
def serials_should_be_shown():
    with step('Serials - are shown'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text, "Сериалы")]')).should(have.text('Сериалы'))
        
        
Для этого локатора сверху тест один:

def confirm_cookie():
    with step('Confirm cookie'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Соглашаюсь"]')).click()


def tap_on_my_ivi():
    with step('Tap on "Мой ivi"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).click()
        
# THEN
    my_ivi.serials_should_be_shown()
    
    
    
    
    
    


def tap_on_recommend_movie():
    with step('Tap on recommend movie'):
        browser.element((
            AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="ru.ivi.client:id/poster"])')).click()


def button_watch_should_be_shown():
    with step('Button "Смотреть" is shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Смотреть"]')).should(have.text('Смотреть'))

def button_auth_should_be_shown():
    with step('Button "Войти или зарегистрироваться" is shown'):
        (browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Войти или зарегистрироваться"]'))
         .should(have.text('Войти или зарегистрироваться')))

def confirm_cookie():
    with step('Confirm cookie'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Соглашаюсь"]')).click()


def tap_on_my_ivi():
    with step('Tap on "Мой ivi"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).click()


def tap_on_profile():
    with step('Tap on "Профиль"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).click()



Для оставшихся трех вроде только последний использован (куки посмотрю убрать может, не видел пока их)

@allure.epic('Profile')
@allure.story('Open profile')
@allure.title('Open profile')
@allure.feature('Profile')
@allure.label('microservice', 'Profile')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_open_profile():
    # WHEN
    base_page.confirm_cookie()
    base_page.tap_on_profile()

    # THEN
    profile.button_auth_should_be_shown()







"""