from __future__ import unicode_literals

from pyvirtualdisplay import Display
from selenium import webdriver

from threading import Timer

from apps.FBTC.page import Homepage

display = Display(visible=0, size=(1366, 768))
display.start()

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.set_window_size(1280, 720)


fbtc = Homepage(browser)
fbtc.visit()

fbtc.login()

import time
time.sleep(5)

def collect():
    fbtc.click_recaptcha()
    fbtc.take_screenshot()
    Timer(3610, collect).start()


collect()


# Timer(3600.0, fbtc.click_recaptcha())
# import time
# time.sleep(5)


# # browser.save_screenshot('channelfix.png')


# browser.quit()
# display.stop()
