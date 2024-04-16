import datetime
import random
import time

import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Create and save project")
class TestCreateProject(BaseTest):

    @allure.title("Create new project")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_new_project(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.click_projects_link()
        self.project_page.add_new_project()
        self.project_page.input_name(f"Test+{datetime.date.today()}")
        self.project_page.click_type_project()
        self.project_page.select_type_project()
        self.project_page.click_type_client()
        self.project_page.select_type_client()
        self.project_page.click_brand()
        self.project_page.select_brand()
        self.project_page.click_start_date()
        self.project_page.select_start_date()
        self.project_page.set_start_date()
        self.project_page.click_end_date()
        time.sleep(1)
        self.project_page.select_end_date()
        #time.sleep(4)
        self.project_page.set_end_date()
        self.project_page.save_project()
        time.sleep(3)
        self.project_page.input_search_new_project(f"Test+{datetime.date.today()}")
        time.sleep(2)
        self.project_page.make_screenshot("Success")


