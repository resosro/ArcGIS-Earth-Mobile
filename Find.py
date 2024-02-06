from imports import *
class Find:

    def __init__(self, driver):
        self.driver = driver

    def name(self, name):
        return self.driver.find_element(by=app.NAME, value=name)

    def x_path(self, XPATH):
        return self.driver.find_element(by=app.XPATH, value=XPATH)

    def class_name(self, class_name):
        return self.driver.find_element(by=app.CLASS_NAME, value=class_name)

    def ID(self, ID):
        return self.driver.find_element(by=app.ID, value=ID)

    def link_text(self, link_text):
        return self.driver.find_element(app.LINK_TEXT, link_text)

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x,start_y,end_x,end_y,duration)
    def accessibility_id(self, a_id):
        return self.driver.find_element(app.ACCESSIBILITY_ID, a_id )
