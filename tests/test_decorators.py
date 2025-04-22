import allure
from allure_commons.types import Severity
from selene import browser, by, have
from selene.support.shared.jquery_style import s

@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_decorator_steps(setup_browser):
    open_main_page()
    search_for_repository("aliranoki/qa_guru_python_19_hw5")
    go_to_repository("aliranoki/qa_guru_python_19_hw5")
    open_issue_tab()
    should_see_issue_with_title("test_issue")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с текстом {text}")
def should_see_issue_with_title(text):
    s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text(text))