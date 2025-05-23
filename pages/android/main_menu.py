from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def close_advertisement():
    with step("Close annoying advertisement"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Закрыть лист')).click()

def button_my_ivi_should_be_visible():
    with step('Button "Мой ivi" is visible'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'my_ivi')).should(be.visible)


def button_search_should_be_visible():
    with step('Button "Поиск" is visible'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'search')).should(be.visible)


def button_stream_should_be_visible():
    with step('Button "Поток" is visible'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'flow')).should(be.visible)


def button_favourite_should_be_visible():
    with step('Button "Избранное" is visible'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'favourites')).should(be.visible)


def button_profile_should_be_visible():
    with step('Button "Войти" is visible'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'profile')).should(be.visible)


def search_function_and_verify_result(text):
    with step("Search function use and verify result"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'search')).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.EditText")).type(text)
        browser.element((AppiumBy.XPATH, "(//android.view.View[@resource-id='DsKitPoster'])[1]")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, text)).should(be.visible)


def profile_page(email, password):
    with step("Test profile page, authorization"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'profile')).click()
        browser.element((AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[1]")).click()
        browser.element((AppiumBy.ID, "ru.ivi.client:id/etInput")).type(email)
        browser.element((AppiumBy.ID, 'ru.ivi.client:id/btnAction')).click()
        try:
            browser.element((AppiumBy.ID, "ru.ivi.client:id/switch_to_sms")).click()
        except Exception:
            pass
        browser.element((AppiumBy.ID, "ru.ivi.client:id/etInput")).type(password)
        browser.element((AppiumBy.ID, 'ru.ivi.client:id/btnAction')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "profile")).should(have.text('max.nvo06'))