from __future__ import unicode_literals

from pyvirtualdisplay import Display
from selenium import webdriver

from apps.FBTC.page import Homepage

display = Display(visible=0, size=(1366, 768))
display.start()

browser = webdriver.Chrome()
browser.set_window_size(1280, 720)


fbtc = Homepage(browser)
fbtc.visit()

import time
time.sleep(5)

fbtc.take_screenshot()

# browser.save_screenshot('channelfix.png')


browser.quit()
display.stop()