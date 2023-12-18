from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time


class SkillFilteration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_filter(self):
        col_filter = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Show filters"]')
        col_filter.click()
        time.sleep(3)
        col_filter_elements1 = self.driver.find_elements(By.TAG_NAME, 'select')
        for element_opt in col_filter_elements1:
            element_opt.click()
            time.sleep(3)
            print(element_opt.get_attribute('innerHTML'))

        # col_filter_element_items1 = col_filter_elements1.find_elements(By.TAG_NAME, 'select')
        # col_filter_element_items1.click()
        # time.sleep(4)


