import pytest

from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.projects_page import ProjectsPage


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    project_page: ProjectsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.project_page = ProjectsPage(driver)
