from __future__ import unicode_literals

import getpass
import time
from datetime import datetime

from selenium.webdriver.common.keys import Keys

from core.slugify import slugify


from core.page import BasePage


class Homepage(BasePage):
    url = 'https://freebitco.in/?op=home'

    def login(self):
        email = str(input('Email:'))
        password = getpass.getpass()
        code = str(input('2FA:'))

        login_btn = self.driver.find_element_by_css_selector(
            '.login_menu_button>a')
        login_btn.click()

        time.sleep(5)

        email_field = self.driver.find_element_by_id('login_form_btc_address')
        password_field = self.driver.find_element_by_id('login_form_password')
        code_field = self.driver.find_element_by_id('login_form_2fa')


        email_field.send_keys(email)
        password_field.send_keys(password)
        code_field.send_keys(code)
        self.take_screenshot()
        self.driver.find_element_by_id('login_button').click()
        self.take_screenshot()

    def click_recaptcha(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.take_screenshot()
        self.driver.execute_script('$(\'.recaptcha-checkbox-checkmark\').click()')
        # checkbox = self.driver.find_element_by_css_selector('.recaptcha-checkbox-checkmark')
        # checkbox.click()

        time.sleep(2)

        claim_btn = self.driver.find_element_by_id('free_play_form_button')
        claim_btn.click()

        self.take_screenshot()

    def take_screenshot(self):
        self.driver.save_screenshot(
            '{}{}-{}.png'.format(
                self.base_dir, 'fbtc', slugify(datetime.now().isoformat())))
