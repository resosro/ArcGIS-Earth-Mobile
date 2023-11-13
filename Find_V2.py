from imports import *

# Class to abstract away so scripts can be run through a single object
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

