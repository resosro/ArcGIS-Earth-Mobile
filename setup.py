from imports import *

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


def setUp(self) -> None:
    # creates instance of webdriver remote which allows us to use methods of selenium
    self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    self.window = self.driver.get_window_size()
    self.height = self.window.get('height')
    self.width = self.window.get('width')
    self.right_side = self.width - (self.width * 0.2)
    self.left_side = self.width - (self.width * 0.8)
    self.middle_of_screen = self.height * .5
    # creates instance of find from framework and is able to access those methods using the driver that
    # we instantiated here
    global find_by
    find_by = Find(self.driver)