from __future__ import unicode_literals

from pyvirtualdisplay import Display
from selenium import webdriver

from threading import Timer

from apps.FBTC.page import Homepage

display = Display(visible=0, size=(1366, 768))
display.start()

browser = webdriver.Firefox()
browser.set_window_size(1280, 720)


fbtc = Homepage(browser)
fbtc.visit()

fbtc.login()


def collect():
    fbtc.take_screenshot()
    fbtc.click_recaptcha()
    Timer(3610, collect).start()


collect()


# Timer(3600.0, fbtc.click_recaptcha())
# import time
# time.sleep(5)


# # browser.save_screenshot('channelfix.png')


# browser.quit()
# display.stop()
