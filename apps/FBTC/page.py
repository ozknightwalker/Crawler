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
        login_btn = self.driver.find_element_by_css_selector(
            '.login_menu_button>a')
        login_btn.click()

        email_field = self.driver.find_element_by_id('login_form_btc_address')
        password_field = self.driver.find_element_by_id('login_form_password')
        code_field = self.driver.find_element_by_id('login_form_2fa')

        email = str(input('Email:'))
        password = getpass.getpass()
        code = str(input('2FA:'))

        print(email, code)

        email_field.send_keys(email)
        password_field.send_keys(password)
        code_field.send_keys(code)
        self.driver.find_element_by_id('login_button').click()

    def click_recaptcha(self):
        time.sleep(2)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        checkbox = self.driver.find_element_by_id('recaptcha-anchor')
        checkbox.click()

        time.sleep(2)

        claim_btn = self.driver.find_element_by_id('free_play_form_button')
        claim_btn.click()

    def take_screenshot(self):
        self.driver.save_screenshot(
            '{}{}-{}.png'.format(
                self.base_dir, 'fbtc', slugify(datetime.now().isoformat())))
