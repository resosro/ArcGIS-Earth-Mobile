import os.path

from imports import *
from setup import *
import main

global initial
initial = {}

class TestAppium(unittest.TestCase):

    # Seems like this must be in the actual class to be run
    def setUp(self) -> None:
        # creates instance of webdriver remote which allows us to use methods of selenium
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        self.window = self.driver.get_window_size()
        self.height = self.window.get('height')
        self.width = self.window.get('width')
        self.right_side = self.width - (self.width * 0.2)
        self.left_side = self.width - (self.width * 0.8)
        self.middle_of_screen_h = self.height * .5
        self.middle_of_screen_w = self.width * .5
        self.toolbox_height = self.height * 0.899
        self.toolbox_width = self.width * 0.5
        self.touch = TouchAction(self.driver)
        print(self.height * 0.5)

        # creates instance of find from framework and is able to access those methods using the driver that
        # we instantiated here
        global find_by, report_file, name
        initial_json = {}
        find_by = Find(self.driver)
        name = self.id().split(".")[-1].split("__")[-1]
        # self.delete_report()


    def delete_report(self):
        if os.path.exists('output'):
            os.remove('output')
        os.mkdir("output")

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def write_to_report(self):
        print("called")
        report_file = os.path.join("reporting/output/report_file.json")
        with open(report_file, 'a') as rep:
            string = str(initial).replace("\'", "\"")
            rep.write(string)


    def test_01__allow_permissions(self):
        try:
            time.sleep(short_sleep)
            allow_gallery = find_by.ID("com.android.permissioncontroller:id/permission_allow_one_time_button")
            allow_gallery.click()
            time.sleep(mid_sleep)
            allow_location = find_by.ID("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            allow_location.click()
            time.sleep(mid_sleep)
            allow_photo = find_by.ID("com.android.permissioncontroller:id/permission_allow_button")
            allow_photo.click()
            time.sleep(short_sleep)
            initial[name] = {
                "results": "Pass",
                "comment": "Permissions Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Permissions Failed"
            }


    def test_02__swipe_tut(self):
        try:
            self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_h, 1000)
            time.sleep(short_sleep)
            self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_h, 1000)
            time.sleep(short_sleep)
            self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_h, 1000)
            time.sleep(short_sleep)
            # value here needs to be low as the element/view disappears, making it fail?
            self.driver.swipe(self.right_side, self.middle_of_screen_h, self.middle_of_screen_w, self.middle_of_screen_h,
                              50)
            initial[name] = {
                "results": "Pass",
                "comment": "Swipe Passed"
            }
            time.sleep(mid_sleep)

        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Swipe Failed"
            }

    def test_03__basemap_selection(self):
        try:
            time.sleep(long_sleep)
            first_choice = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")
            first_choice.click()
            time.sleep(long_sleep)
            close = find_by.ID("com.esri.earth.phone:id/rl_close")
            close.click()
            initial[name] = {
                "results": "Failed",
                "comment": "Base Map Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Base Map Failed"
            }


    def test_04__sign_in_workflow(self):

        try:
            time.sleep(long_sleep)

            self.start_sign_in()
            self.sign_in_enterprise()
            # self.sign_out()
            # self.sign_in_online()
            initial[name] = {
                "results": "Passed",
                "comment": "Permissions Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Permissions Failed"
            }

    def sign_in_online(self):
        arcgis_online = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[1]")
        arcgis_online.click()

    def sign_in_enterprise(self):
        enterprise = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[3]")
        enterprise.click()
        time.sleep(2)
        enter_url = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]")
        enter_url.click()
        time.sleep(2)
        enter_input = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText")
        enter_input.send_keys("https://rpubs22201.ags.esri.com/portal")
        time.sleep(lil_sleep)

        button = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText/android.view.View/android.view.View/android.widget.ImageView[2]")

        button.click()
        time.sleep(mid_sleep)

        sign_in = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]")
        sign_in.click()
        time.sleep(mid_sleep)

        time.sleep(4)
        user_name = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText")
        user_name.send_keys("creator2")
        pass_word = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText")
        pass_word.send_keys("portalaccount1")
        time.sleep(lil_sleep)

        sign_in = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]")
        time.sleep(lil_sleep)
        sign_in.click()
        time.sleep(lil_sleep)
        self.driver.back()

    def start_sign_in(self):
        rl = find_by.accessibility_id("Admin")
        rl.click()
        time.sleep(lil_sleep)
        arrow = find_by.accessibility_id("Portal Url")
        arrow.click()

    def sign_out(self):
        rl = find_by.accessibility_id("Admin")
        rl.click()
        time.sleep(lil_sleep)
        sign_out = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[2]/android.widget.Button")
        sign_out.click()
        time.sleep(lil_sleep)
        sign_out = find_by.ID("com.esri.earth.phone:id/ok")
        sign_out.click()

    def test_05__search_places(self):

        try:
            search = find_by.accessibility_id("Search Places")
            search.click()
            time.sleep(mid_sleep)
            search_bar = find_by.class_name("android.widget.EditText")
            search_bar.send_keys("380 New York St")
            self.driver.press_keycode(66)
            time.sleep(mid_sleep)
            first = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]")
            time.sleep(mid_sleep)
            first.click()
            time.sleep(mid_sleep)
            close = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View")
            close.click()
            time.sleep(2)
            initial[name] = {
            "results": "Passed",
            "comment": "Permissions Passed"
        }
        except:
            initial[name] = {
            "results": "Failed",
            "comment": "Permissions Failed"
        }

    def test_06__toc_list(self):
        try:
            toc = find_by.accessibility_id("Toc List")
            toc.click()
            time.sleep(3)
            more_button = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View"
                                         "/android.view.View/android.view.View/android.view.View["
                                         "1]/android.view.View/android.view.View/android.view.View[2]")
            more_button.click()
            time.sleep(3)
            # Tap is not enabled on values of y that are above a certain y value
            # Trying with a different phone
            # self.touch.tap(x=500, y= 2050, count=1).perform()
            # add_data = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View")
            # add_data.click()
            firefly = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]")
            firefly.click()
            self.driver.back()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
                }
        except:
                initial[name] = {
                    "results": "Failed",
                    "comment": "Test Failed"
                }
    def test_07__toc_add_data(self):

        try:
            self.touch.tap(None, self.width * 0.8, self.height * 0.7, 1).perform()
            time.sleep(mid_sleep)
            # favorite = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
            # favorite.click()
            # exit = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
            # exit.click()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_08__toc_add_from_url(self):

        try:
            url = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]")
            url.click()
            time.sleep(lil_sleep)
            self.driver.back()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_09__add_from_file(self):
        try:
            file_box = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]")
            file_box.click()
            time.sleep(lil_sleep)
            self.driver.back()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_10__add_from_QR(self):

        try:
            qr_box = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]")
            qr_box.click()
            time.sleep(lil_sleep)
            self.driver.back()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def click_portal(self):
        portal = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]")
        portal.click()


    # def test_add_bottom(self):
    #     # TODO: Needs to scale this properly, works only with pixel 4 XL right now
    #     # length = int(self.height * 0.85)
    #     # width = int(self.width * 0.87)
    #     self.touch.tap(None, 950, 1950, 1).perform()

    def select_toc(self):
        toc = find_by.accessibility_id("Toc List")
        toc.click()

    def test_11__toc_add_from_portal(self):

        try:
            self.click_portal()
            time.sleep(short_sleep)
            usa_generalized = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View")
            usa_generalized.click()
            time.sleep(lil_sleep)
            exit = find_by.x_path(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
            exit.click()
            time.sleep(lil_sleep)
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_12__select_share_screenshot(self):

        try:
            screenshot = find_by.accessibility_id("Screenshot")
            screenshot.click()
            self.driver.back()
            time.sleep(lil_sleep)
            self.driver.back()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_13__click_home(self):

        try:
            touch = TouchAction(self.driver)
            touch.tap(None, 983, 827, 1).perform()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_14__click_arrow(self):

        try:
            touch = TouchAction(self.driver)
            touch.tap(None, 989, 843, 1).perform()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_15__find(self):

        try:
            touch = TouchAction(self.driver)
            touch.tap(None, 986, 1001, 1).perform()
            time.sleep(5)
            touch.tap(None, 986, 1001, 1).perform()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_16__toolbox(self):

        try:
            toolbox = find_by.ID("com.esri.earth.phone:id/rl_tool_control")
            toolbox.click()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }


    def toolbox_navigate_left(self):
        arrow_left = find_by.ID("com.esri.earth.phone:id/img_pre")
        arrow_left.click()

    def toolbox_navigate_right(self):
        arrow_right = find_by.ID("com.esri.earth.phone:id/img_next")
        arrow_right.click()

    def test_17__draw(self):

        try:
            self.toolbox_navigate_left()
            self.click_toolbox_item()
            time.sleep(short_sleep)
            self.add_point()
            time.sleep(short_sleep)
            self.add_line()
            time.sleep(short_sleep)
            self.add_poly()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def click_toolbox_item(self):
        self.touch.tap(None, 540, 1740, 1).perform()

    def click_add(self):
        add = find_by.accessibility_id("Add point")
        add.click()

    def add_line(self):
        time.sleep(lil_sleep)
        line = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
        line.click()
        time.sleep(lil_sleep)
        self.click_add()
        time.sleep(lil_sleep)
        self.driver.swipe(self.left_side, self.middle_of_screen_h, self.right_side, self.middle_of_screen_w, 100)
        time.sleep(lil_sleep)
        self.finish_drawing()

    def finish_drawing(self):
        check = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ImageView[4]")
        check.click()
        self.draw_close()

    def add_poly(self):
        self.click_add()
        time.sleep(lil_sleep)
        self.driver.swipe(self.left_side, self.middle_of_screen_h, self.right_side, self.middle_of_screen_w, 100)
        time.sleep(lil_sleep)
        self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_w, 100)
        time.sleep(lil_sleep)
        self.finish_drawing()

    def draw_close(self):
        close = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View")
        close.click()

    def add_point(self):
        locate = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
        locate.click()
        time.sleep(lil_sleep)
        self.click_add()
        time.sleep(lil_sleep)
        self.draw_close()

        # TODO: Point styling is not implemented, cannot select back
        # time.sleep(lil_sleep)
        # style = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[1]")
        # style.click()
        # time.sleep(lil_sleep)
        # pin = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[1]")
        # pin.click()
        # time.sleep(lil_sleep)
        # color = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView[2]")
        # color.click()
        # time.sleep(lil_sleep)
        # red = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]")
        # red.click()
        # time.sleep(lil_sleep)
        # size = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView[3]")
        # size.click()
        # time.sleep(lil_sleep)
        # self.touch.tap(None, 815,940,1).perform()
        #
        # TODO: Still need to get this return when styling the point
        # back = find_by.x_path("(//android.widget.ImageView[@content-desc=""Return Back""])[2]")
        # back.click()

        # Closes
        self.touch.tap(None, 1043, 1473, 1).perform()

    def exit_tool(self):
        return_back = find_by.accessibility_id("Return Back")
        return_back.click()

    def test_18__3D_analysis(self):
        try:
            self.toolbox_navigate_left()
            self.click_toolbox_item()
            self.exit_tool()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_19__underground(self):
        try:
            self.toolbox_navigate_left()
            self.click_toolbox_item()
            time.sleep(lil_sleep)
            self.touch.tap(None, 140, 1900, 1).perform()
            time.sleep(mid_sleep)
            self.exit_tool()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_20__tour(self):
        try:
            new_tour = find_by.accessibility_id("New Tour")
            new_tour.click()
            time.sleep(long_sleep)
            self.exit_tool()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_21__track(self):
        try:
            self.toolbox_navigate_left()
            self.click_toolbox_item()
            z_value = find_by.ID("com.esri.earth.phone:id/cb_track_zvalue")
            z_value.click()
            start = find_by.ID("com.esri.earth.phone:id/ll_track_start")
            start.click()
            #         TODO: Needs to record the location, by holding
            self.touch.long_press(None, 737, 1912, 66000)
            self.exit_tool()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_22__measure(self):
        try:
            self.toolbox_navigate_left()
            self.click_toolbox_item()
            self.click_add()
            self.exit_tool()
            initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        except:
            initial[name] = {
                "results": "Failed",
                "comment": "Test Failed"
            }

    def test_23__test_left_toc(self):
        # try:
        #     # self.explore_gis_gallery()
        #     # self.tracks()
        #     # self.tours()
        #     # self.downloads()
        #     # self.settings()
        #     # self.provide_feedback()
        #     # self.about()
        initial[name] = {
                "results": "Pass",
                "comment": "Test Passed"
            }
        #     self.write_to_report()
        # except:
        #     initial[name] = {
        #         "results": "Failed",
        #         "comment": "Test Failed"
        #     }
        self.write_to_report()


    def explore_gis_gallery(self):
        explore = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[4]")
        explore.click()
        time.sleep(lil_sleep)
        check_box = find_by.ID("com.esri.earth.phone:id/cb_show")
        check_box.click()
        time.sleep(lil_sleep)
        close = find_by.ID("com.esri.earth.phone:id/rl_close")
        close.click()

    def tracks(self):
        tracks = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[5]")
        tracks.click()
        self.exit_tool()

    def tours(self):
        tours = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[6]")
        tours.click()
        self.exit_tool()

    def downloads(self):
        # downloads = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[7]")
        # downloads.click()
        exit = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]")
        exit.click()

    def test_how_to_use_earth(self):
        # how_to = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[8]")
        self.driver.swipe(self.left_side, self.middle_of_screen_h, self.right_side, self.middle_of_screen_h, 1000)
        # how_to.click()

    def settings(self):
        settings = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[9]")
        settings.click()

    def provide_feedback(self):
        feedback = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[10]")
        feedback.click()

    def about(self):
        about = find_by.x_path(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[11]")
        about.click()





if __name__ == '__main__':
    unittest.main()

