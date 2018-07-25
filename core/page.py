from __future__ import unicode_literals

from .slugify import slugify


class BasePage(object):
    url = ''
    base_dir = './screenshots/'

    def __init__(self, driver):
        self.driver = driver


    def visit(self):
        self.driver.get(self.url)

    def take_screenshot(self):
        self.driver.save_screenshot(
            '{}{}.png'.format(self.base_dir, slugify(self.driver.title)))


