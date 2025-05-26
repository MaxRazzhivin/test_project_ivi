from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def close_advertisement():
    with step("Close annoying advertisement"):
        try:
            browser.element((AppiumBy.ACCESSIBILITY_ID, "back")).click()
        except Exception:
            pass

def button_my_ivi_should_be_visible():
    with step('Button "Мой ivi" is visible'):
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Мой Иви; вкладка"')).should(be.visible)


def button_search_should_be_visible():
    with step('Button "Поиск" is visible'):
        browser.element((AppiumBy.XPATH, '//XCUIElementTypeOther[@name="VoiceOverElement" and @label="Поиск; вкладка"]')).should(be.visible)


def button_stream_should_be_visible():
    with step('Button "Поток" is visible'):
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Поток; вкладка"')).should(be.visible)


def button_favourite_should_be_visible():
    with step('Button "Избранное" is visible'):
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Избранное; вкладка"')).should(be.visible)


def button_profile_should_be_visible():
    with step('Button "Войти" is visible'):
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Войти; вкладка"')).should(be.visible)


def buttons_of_header_section_are_clickable():
    with step("Buttons from header are active"):
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Русские"')).click()
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Зарубежные"')).click()
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Комедии"')).click()
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Драмы"')).click()
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Семейные"')).click()







def search_function_and_verify_result(text):
    with step("Search function use and verify result"):
        browser.element((AppiumBy.XPATH, '//XCUIElementTypeOther[@name="VoiceOverElement" and @label="Поиск; вкладка"]')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Input")).type(text)
        browser.element((AppiumBy.IOS_PREDICATE, "name == 'VoiceOverElement' AND label == 'Достать ножи; выбор Иви; Бесплатно'")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "contentView")).should(have.text(text))


def profile_page(email, password):
    with step("Test profile page, authorization"):
        browser.element((AppiumBy.IOS_PREDICATE, 'name == "VoiceOverElement" AND label == "Войти; вкладка"')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Input")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Input")).type(email)
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Button')).click()
        try:
            browser.element((AppiumBy.IOS_PREDICATE, "name == 'VoiceOverElement' AND label == 'Ввести пароль'")).click()
        except Exception:
            pass
        browser.element((AppiumBy.IOS_PREDICATE, "name == 'editbox'")).send_keys(password)
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "logout")).click()
        browser.element((AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="VoiceOverElement"])[7]')).click()
