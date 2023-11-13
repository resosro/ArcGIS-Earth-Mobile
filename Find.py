from appium.webdriver.common.appiumby import AppiumBy as app

# This class essentially is created to simplify find calls
# find is instantiated so we can use these methods and call each of them through an object
# Each method uses a selenium method which searches the dom for the item and selects it, so it returns the item
class Find:

    def __init__(self, driver):
        self.driver = driver

    def name(self, name):
        return self.driver.find_element(by=app.NAME, value=name)

    def x_path(self, XPATH):
        return self.driver.find_element(by=app.XPATH, value=XPATH)

    def ID(self, ID):
        return self.driver.find_element(by = app.ID, value = ID)

    def link_text(self, link_text):
        return self.driver.find_element(app.LINK_TEXT, link_text)

