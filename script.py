from imports import *
from setup import *

import sys
sys.path.append(r'\\ragsauto01\arcgis_codeshare')
import results_report

if pc_report_file:
    if os.path.isfile(pc_report_file):
        if ln_exit_code == 0:
            results_report.main(“c:\temp\results_report.json”, "Publish Shape File via Portal", "Pass", "Successfully published file”)
        else:
            results_report.main(“c:\temp\results_report.json”, "Publish Shape File via Portal", "Fail", "Failed to publish file”)
    else:
        print("Report file not found: " + pc_report_file)
 
# Once you have the JSON file you can generate the XML file to upload by using this script:
python "\\ragsauto01\arcgis_codeshare\write_sanity_report_xml.py" 5008 "c:\temp\agend_report_header.json" “c:\temp\results_report.json” “c:\temp\ArcGIS Enterprise on Kubernetes Confidence Tests - AZURE.xml” “c:\temp\ArcGIS Enterprise on Kubernetes Confidence Tests - AZURE Complete.xml”

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
        global find_by
        find_by = Find(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


    def test_02_allow_permissions(self):
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


    def test_03_swipe_tut(self):
        self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_h, 1000)
        time.sleep(short_sleep)
        self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_h, 1000)
        time.sleep(short_sleep)
        self.driver.swipe(self.right_side, self.middle_of_screen_h, self.left_side, self.middle_of_screen_h, 1000)
        time.sleep(short_sleep)
        # value here needs to be low as the element/view disappears, making it fail?
        self.driver.swipe(self.right_side, self.middle_of_screen_h, self.middle_of_screen_w, self.middle_of_screen_h, 50)
        time.sleep(short_sleep)


    def test_04_basemap_selection(self):
        # time.sleep(mid_sleep)
        # # removed in 2.0
        # # skip_button = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View")
        # # skip_button.click()
        # first_choice = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")
        # first_choice.click()
        time.sleep(short_sleep)
        close = find_by.ID("com.esri.earth.phone:id/rl_close")
        close.click()

    def test_05_sign_in_workflow(self):
        self.start_sign_in()
        self.sign_in_enterprise()
        # self.sign_out()
        # self.sign_in_online()


    def sign_in_online(self):
        arcgis_online = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[1]")
        arcgis_online.click()



    def sign_in_enterprise(self):
        enterprise = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[3]")
        enterprise.click()
        time.sleep(2)
        enter_url = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]")
        enter_url.click()
        time.sleep(2)
        enter_input = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText")
        enter_input.send_keys("https://rpubs22201.ags.esri.com/portal")
        time.sleep(lil_sleep)

        button = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText/android.view.View/android.view.View/android.widget.ImageView[2]")

        button.click()
        time.sleep(mid_sleep)

        sign_in = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]")
        sign_in.click()
        time.sleep(mid_sleep)

        time.sleep(4)
        user_name = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText")
        user_name.send_keys("creator2")
        pass_word = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText")
        pass_word.send_keys("portalaccount1")
        time.sleep(lil_sleep)

        sign_in = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]")
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
        sign_out = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[2]/android.widget.Button")
        sign_out.click()
        time.sleep(lil_sleep)
        sign_out = find_by.ID("com.esri.earth.phone:id/ok")
        sign_out.click()


    def test_06_search_places(self):
        search = find_by.accessibility_id("Search Places")
        search.click()
        time.sleep(mid_sleep)
        search_bar = find_by.class_name("android.widget.EditText")
        search_bar.send_keys("380 New York St")
        self.driver.press_keycode(66)
        time.sleep(mid_sleep)
        first = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]")
        time.sleep(mid_sleep)
        first.click()
        time.sleep(mid_sleep)

        close = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View")
        close.click()
        time.sleep(2)
    def test_07_toc_list(self):
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
        firefly = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]")
        firefly.click()
        self.driver.back()

    def test_08_toc_add_data(self):
        self.touch.tap(None, self.width * 0.8, self.height*0.7, 1).perform()
        time.sleep(mid_sleep)
        # favorite = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
        # favorite.click()
        # exit = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        # exit.click()

    def test_09_toc_add_from_url(self):
        url = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]")
        url.click()
        time.sleep(lil_sleep)
        self.driver.back()
    def test_10_add_from_file(self):
        file_box = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]")
        file_box.click()
        time.sleep(lil_sleep)
        self.driver.back()

    def test_11_add_from_QR(self):
        qr_box = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]")
        qr_box.click()
        time.sleep(lil_sleep)
        self.driver.back()



    def click_portal(self):
        portal = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]")
        portal.click()
    def test_12_toc_add_from_portal(self):
        self.click_portal()
        time.sleep(short_sleep)
        usa_generalized = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View")
        usa_generalized.click()
        time.sleep(lil_sleep)
        exit = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        exit.click()
        time.sleep(lil_sleep)



    # def test_add_bottom(self):
    #     # TODO: Needs to scale this properly, works only with pixel 4 XL right now
    #     # length = int(self.height * 0.85)
    #     # width = int(self.width * 0.87)
    #     self.touch.tap(None, 950, 1950, 1).perform()


    def select_toc(self):
        toc = find_by.accessibility_id("Toc List")
        toc.click()


    def test_13_select_share_screenshot(self):
        screenshot = find_by.accessibility_id("Screenshot")
        screenshot.click()
        self.driver.back()
        time.sleep(lil_sleep)
        self.driver.back()


    def test_14_click_home(self):
        touch = TouchAction(self.driver)
        touch.tap(None, 983,827,1).perform()

    def test_15_click_arrow(self):
        touch = TouchAction(self.driver)
        touch.tap(None, 989,843,1).perform()

    def test_16_find(self):
        touch = TouchAction(self.driver)
        touch.tap(None, 986,1001,1).perform()
        time.sleep(5)
        touch.tap(None, 986,1001,1).perform()

    def test_17_toolbox(self):
        toolbox = find_by.ID("com.esri.earth.phone:id/rl_tool_control")
        toolbox.click()


    def toolbox_navigate_left(self):
        arrow_left = find_by.ID("com.esri.earth.phone:id/img_pre")
        arrow_left.click()

    def toolbox_navigate_right(self):
        arrow_right = find_by.ID("com.esri.earth.phone:id/img_next")
        arrow_right.click()
    def test_18_draw(self):
        self.toolbox_navigate_left()
        self.click_toolbox_item()
        time.sleep(short_sleep)
        self.add_point()
        time.sleep(short_sleep)
        self.add_line()
        time.sleep(short_sleep)
        self.add_poly()

    def click_toolbox_item(self):
        self.touch.tap(None,540,1740, 1).perform()

    def click_add(self):
        add = find_by.accessibility_id("Add point")
        add.click()

    def add_line(self):
        time.sleep(lil_sleep)
        line = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
        line.click()
        time.sleep(lil_sleep)
        self.click_add()
        time.sleep(lil_sleep)
        self.driver.swipe(self.left_side, self.middle_of_screen_h, self.right_side, self.middle_of_screen_w, 100)
        time.sleep(lil_sleep)
        self.finish_drawing()



    def finish_drawing(self):
        check = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ImageView[4]")
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
        locate = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
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

        # TODO: Still need to get this return when styling the point
        # back = find_by.x_path("(//android.widget.ImageView[@content-desc=""Return Back""])[2]")
        # back.click()

        # Closes
        self.touch.tap(None, 1043, 1473, 1).perform()

    def exit_tool(self):
        return_back = find_by.accessibility_id("Return Back")
        return_back.click()

    def test_19_3D_analysis(self):
        self.toolbox_navigate_left()
        self.click_toolbox_item()
        self.exit_tool()

    def test_20_underground(self):
        self.toolbox_navigate_left()
        self.click_toolbox_item()
        time.sleep(lil_sleep)
        self.touch.tap(None, 140, 1900, 1).perform()
        time.sleep(mid_sleep)
        self.exit_tool()

    def test_21_tour(self):
        # self.toolbox_navigate_left()
        # self.click_toolbox_item()
        # select_placemark = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]")
        # select_placemark.click()

        # first = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]")
        # for i in range(1, 3, 1):
        #     f_path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[{b}]".format(b = i)
        #     element = find_by.x_path(f_path)
        #     element.click()
        # done = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView[2]")
        # done.click()
        #
        # save_button = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]")
        # save_button.click()
        new_tour = find_by.accessibility_id("New Tour")
        new_tour.click()
        # TODO: Need to try out the actual pause, stop and change speed
        time.sleep(long_sleep)
        self.exit_tool()

    def test_22_track(self):
        self.toolbox_navigate_left()
        self.click_toolbox_item()
        z_value = find_by.ID("com.esri.earth.phone:id/cb_track_zvalue")
        z_value.click()
        start = find_by.ID("com.esri.earth.phone:id/ll_track_start")
        start.click()
#         TODO: Needs to record the location, by holding
        self.touch.long_press(None, 737, 1912, 66000)
        self.exit_tool()

    def test_23_measure(self):
        self.toolbox_navigate_left()
        self.click_toolbox_item()
        self.click_add()
        self.exit_tool()

    def test_24_test_left_toc(self):
        self.explore_gis_gallery()
        self.tracks()
        self.tours()
        self.downloads()
        self.settings()
        self.provide_feedback()
        self.about()


    def explore_gis_gallery(self):
        explore = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[4]")
        explore.click()
        time.sleep(lil_sleep)
        check_box = find_by.ID("com.esri.earth.phone:id/cb_show")
        check_box.click()
        time.sleep(lil_sleep)
        close = find_by.ID("com.esri.earth.phone:id/rl_close")
        close.click()

    def tracks(self):
        tracks = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[5]")
        tracks.click()
        self.exit_tool()


    def tours(self):
        tours = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[6]")
        tours.click()
        self.exit_tool()

    def downloads(self):
        # downloads = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[7]")
        # downloads.click()
        exit = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]")
        exit.click()

    def test_how_to_use_earth(self):
        # how_to = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[8]")
        self.driver.swipe(self.left_side, self.middle_of_screen_h, self.right_side ,self.middle_of_screen_h, 1000)
        # how_to.click()
    def settings(self):
        settings = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[9]")
        settings.click()
    def provide_feedback(self):
        feedback = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[10]")
        feedback.click()
    def about(self):
        about = find_by.x_path("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[11]")
        about.click()



def generate_report():
    if pc_report_file:
    if os.path.isfile(pc_report_file):
        if ln_exit_code == 0:
            results_report.main(“c:\temp\results_report.json”, "Publish Shape File via Portal", "Pass", "Successfully published file”)
        else:
            results_report.main(“c:\temp\results_report.json”, "Publish Shape File via Portal", "Fail", "Failed to publish file”)
    else:
        print("Report file not found: " + pc_report_file)




if __name__ == '__main__':
    unittest.main()
    generate_report()
    python "\\ragsauto01\\arcgis_codeshare\write_sanity_report_xml.py" 5008 "c:\\temp\\agend_report_header.json" "c:\\temp\\results_report.json” “c:\\temp\ArcGIS Enterprise on Kubernetes Confidence Tests - AZUR.xml” “c:\\temp\ArcGIS Enterprise on Kubernetes Confidence Tests - AZUR Complete.xml”

