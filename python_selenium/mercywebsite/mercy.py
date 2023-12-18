import os
import mercywebsite.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from mercywebsite.SkillFilteration import SkillFilteration
class Mercy(webdriver.Chrome):
    def __init__(self, driver_path=r"/Users/newaccount/PycharmProjects", teardown=False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown = teardown
        super(Mercy, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_mode(self, selector):
        mode_element = self.find_element(By.CSS_SELECTOR, 'svg[data-testid="DarkModeOutlinedIcon"]')
        mode_element.click()
        print("DarkMode clicked")
        time.sleep(4)
        selected_element = self.find_element(By.CSS_SELECTOR, selector)
        selected_element.click()
        print("Changed back to Light Mode")
        time.sleep(4)

    def toggle_menu(self, menu):
        menu_btn = self.find_element(By.CSS_SELECTOR, menu)
        menu_btn.click()
        print("Menu button Closed")
        time.sleep(5)
        # menu_btn_open = self.find_element(By.CSS_SELECTOR, menu)
        # menu_btn_open.click()
        # print("Menu button Opened")
        # time.sleep(5)

    def click_on_sidebar(self, id_name):
        sidebar_toggle = self.find_element(By.ID, id_name)
        sidebar_toggle.click()
        if id_name == "calender":
            self.click_date()
        if id_name == "skill":
            self.add_filter()

        time.sleep(3)

    def click_date(self):
        select_date = self.find_element(By.CSS_SELECTOR, 'td[data-date="2023-04-04"]')
        select_date.click()
        print("Date clciked")
        time.sleep(5)

    def add_filter(self):
        filter_element = SkillFilteration(driver=self)
        filter_element.apply_filter()