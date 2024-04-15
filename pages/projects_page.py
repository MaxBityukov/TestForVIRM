import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class ProjectsPage(BasePage):

    PAGE_URL = Links.PROJECTS_PAGE

    ADD_PROJECT_BUTTON = ("xpath", "//div[text()='Добавить проект']")

    NAME_PROJECT_FIELD = ("xpath", "//input[@aria-label='Название']")
    TYPE_PROJECT_DROPDOWN = ("xpath", "(//i[contains(@class, 'q-select__dropdown')])[4]")
    SELECT_TYPE_PROJECT = ("xpath", "(//div[@class='q-item__label'])[16]")
    TYPE_CLIENT_DROPDOWN = ("xpath", "(//i[contains(@class, 'q-select__dropdown')])[5]")
    SELECT_TYPE_CLIENT = ("xpath", "(//div[@class='q-item__label'])[60]")
    BRAND_DROPDOWN = ("xpath", "(//i[contains(@class, 'q-select__dropdown')])[6]")
    SELECT_BRAND = ("xpath", "(//div[@class='q-item__label'])[16]")
    START_DATE = ("xpath", "(//div[@class='q-field__native row'])[5]")
    START_DAY_BUTTON = ("xpath", "(//div[text()='1'])[2]")
    START_BUTTON_SET = ("xpath", "//div[text()='Установить']")
    END_DATE = ("xpath", "(//div[@class='q-field__native row'])[6]")
    END_DAY_BUTTON = ("xpath", "//div[text()='30']")
    END_BUTTON_SET = ("xpath", "//div[text()='Установить']")
    SAVE_BUTTON = ("xpath", "//div[text()='Сохранить']")
    INPUT_SEARCH_NEW_PROJECT = ("xpath", "//input[@tabindex ='0'][1]")


    @allure.step("Click button add new project")
    def add_new_project(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PROJECT_BUTTON)).click()

    @allure.step("Input name")
    def input_name(self, new_name):
        with allure.step(f"input name '{new_name}'"):
            self.wait.until(EC.element_to_be_clickable(self.NAME_PROJECT_FIELD)).send_keys(new_name)

    @allure.step("Click dropdown type project")
    def click_type_project(self):
        self.wait.until(EC.element_to_be_clickable(self.TYPE_PROJECT_DROPDOWN)).click()

    @allure.step("Select type project")
    def select_type_project(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_TYPE_PROJECT)).click()

    @allure.step("Click dropdown type client")
    def click_type_client(self):
        self.wait.until(EC.element_to_be_clickable(self.TYPE_CLIENT_DROPDOWN)).click()

    @allure.step("Select type project")
    def select_type_client(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_TYPE_CLIENT)).click()

    @allure.step("Click dropdown brand")
    def click_brand(self):
        self.wait.until(EC.element_to_be_clickable(self.BRAND_DROPDOWN)).click()

    @allure.step("Select brand")
    def select_brand(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_BRAND)).click()

    @allure.step("Click by start date")
    def click_start_date(self):
        self.wait.until(EC.element_to_be_clickable(self.START_DATE)).click()

    @allure.step("Select start date")
    def select_start_date(self):
        self.wait.until(EC.element_to_be_clickable(self.START_DAY_BUTTON)).click()

    @allure.step("Set start date")
    def set_start_date(self):
        self.wait.until(EC.element_to_be_clickable(self.START_BUTTON_SET)).click()

    @allure.step("Click by end date")
    def click_end_date(self):
        self.wait.until(EC.element_to_be_clickable(self.END_DATE)).click()

    @allure.step("Select end date")
    def select_end_date(self):
        self.wait.until(EC.element_to_be_clickable(self.END_DAY_BUTTON)).click()

    @allure.step("Set end date")
    def set_end_date(self):
        self.wait.until(EC.element_to_be_clickable(self.END_BUTTON_SET)).click()

    @allure.step("Save project")
    def save_project(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("created new project")
    def input_search_new_project(self, new_project):
        with allure.step(f"input new project '{new_project}'"):
            self.wait.until(EC.element_to_be_clickable(self.INPUT_SEARCH_NEW_PROJECT)).send_keys(new_project)

