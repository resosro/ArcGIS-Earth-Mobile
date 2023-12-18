from imports import *
from appium.options.android import UiAutomator2Options

global long_sleep, short_sleep, mid_sleep, lil_sleep
long_sleep = 20
mid_sleep = 7
short_sleep = 5
lil_sleep = 3

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

