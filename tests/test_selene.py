import allure
from allure_commons.types import Severity
from selene.support import by
from selene import browser, have
from selene.support.shared.jquery_style import s

@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_github(setup_browser):
    browser.open('https://github.com')

    s(".search-input").click()
    s("#query-builder-test").send_keys("aliranoki/qa_guru_python_19_hw5").press_enter()
    s(by.link_text("aliranoki/qa_guru_python_19_hw5")).click()
    s("#issues-tab").click()
    s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text('test_issue'))
