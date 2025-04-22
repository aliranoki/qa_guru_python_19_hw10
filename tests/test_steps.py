import allure
from allure_commons.types import Severity
from selene import have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_dynamic_steps(setup_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("aliranoki/qa_guru_python_19_hw5").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("aliranoki/qa_guru_python_19_hw5")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с текстом 'test_issue'"):
        s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text('test_issue'))

