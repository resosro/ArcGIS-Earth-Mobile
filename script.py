from imports import *
from setup import *

class TestAppium(unittest.TestCase):



    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    # def test(self):
    #     self.driver.find_element(by=app.ID, value="com.esri.earth.phone:id/animator_view").click()
    def test_1_find_gis_earth(self):
        click_app = self.driver.find_element(by=app.XPATH, value="//android.widget.TextView["
                                                                 "@content-desc='ArcGIS Earth']")
        click_app.click()
        time.sleep(short_sleep)

    def test_2_allow_permissions(self):
        time.sleep(2)
        allow_gallery = find_by.ID("com.android.permissioncontroller:id/permission_allow_one_time_button")
        allow_gallery.click()
        allow_location = find_by.ID("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        allow_location.click()
        allow_gallery = find_by.ID("com.android.permissioncontroller:id/permission_allow_button")
        allow_gallery.click()

    def test_3_swipe_tut(self):
        self.driver.swipe(self.right_side, self.middle_of_screen, self.left_side, self.middle_of_screen, 100)
        self.driver.swipe(self.right_side, self.middle_of_screen, self.left_side, self.middle_of_screen, 100)
        self.driver.swipe(self.right_side, self.middle_of_screen, self.left_side, self.middle_of_screen, 100)
        self.driver.swipe(self.right_side, self.middle_of_screen, self.left_side, self.middle_of_screen, 100)

    def test_4_basemap_selection(self):
        time.sleep(short_sleep)
        skip_button = self.driver.find_element(by=app.ID, value="com.esri.earth.phone:id/rl_guid_skip")
        skip_button.click()
        time.sleep(long_sleep)

        close = self.driver.find_element(app.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")
        close.click()
        # popup_checkbox = self.driver.find_element(app.ID, "com.esri.earth.phone:id/cb_show")
        # popup_checkbox.click()
        # more_button = self.driver.find_element(app.ID, "com.esri.earth.phone:id/tv_more")
        # more_button.click()
        # base_map = self.driver.find_element(app.ID, "com.esri.earth.phone:id/tv_live_basemaps")
        # base_map.click()
        # time.sleep(mid_sleep)
        #
        # world_top = self.driver.find_element(app.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout")
        # world_top.click()
        time.sleep(long_sleep)

    def test_4_sign_in(self):
        rl = find_by.ID("com.esri.earth.phone:id/rl_admin")
        rl.click()
        time.sleep(lil_sleep)
        sign_in = find_by.ID("com.esri.earth.phone:id/img_icon")
        sign_in.click()
        # Online
        # agis_online = find_by.ID("com.esri.earth.phone:id/tv_online")
        # agis_online.click()

        enterprise = find_by.ID("com.esri.earth.phone:id/tv_enterprise")
        enterprise.click()
        time.sleep(2)
        enter_url = self.driver.find_element(by=app.XPATH,
                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
        enter_url.click()
        enter_input = self.driver.find_element(app.ID, "com.esri.earth.phone:id/et_enterprise_url")
        enter_input.send_keys("https://rpubs22201.ags.esri.com/portal")
        time.sleep(lil_sleep)

        button = self.driver.find_element(app.ID, "com.esri.earth.phone:id/img_basemap_click")

        button.click()
        time.sleep(mid_sleep)

        sign_in = self.driver.find_element(by=app.XPATH,
                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView")
        sign_in.click()
        time.sleep(mid_sleep)
        user_name = self.driver.find_element(by=app.XPATH,
                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText")
        user_name.send_keys("creator2")
        pass_word = self.driver.find_element(app.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText")
        pass_word.send_keys("portalaccount1")
        time.sleep(lil_sleep)

        sign_in = self.driver.find_element(app.XPATH,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Button[1]")
        time.sleep(lil_sleep)
        sign_in.click()
        time.sleep(lil_sleep)
        self.driver.swipe(self.right_side, self.middle_of_screen, self.right_side, self.middle_of_screen, 1)

    def test_5_add_data_from_gallery(self):
        toolbox = self.driver.find_element(app.ID, "com.esri.earth.phone:id/img_tools")
        toolbox.click()
        time.sleep(mid_sleep)
        points = self.driver.find_element(app.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")
        points.click()
        time.sleep(short_sleep)
        self.driver.swipe(self.right_side, self.middle_of_screen, self.left_side, self.middle_of_screen, 1000)
        name = self.driver.find_element(app.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]")

        name.click()
        time.sleep(long_sleep)
        name_input = self.driver.find_element(app.ID, "com.esri.earth.phone:id/et_draw_name_edit")
        name_input.send_keys("Random Test Point here")
        button = self.driver.find_element(app.NAME, "com.esri.earth.phone:id/rl_draw_name_done")
        button.click()
        self.driver.swipe(self.left_side, self.middle_of_screen, self.right_side, 100, 1000)
        time.sleep(mid_sleep)
        add_point = self.driver.find_element(app.ID, "com.esri.earth.phone:id/iv_add_point")
        add_point.click()
        back_button = self.driver.find_element(app.XPATH,
                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        back_button.click()

    def test_6_search(self):
        search = self.driver.find_element(app.ID, "com.esri.earth.phone:id/rl_search_place")
        search.click()
        time.sleep(lil_sleep)
        search_input = self.driver.find_element(app.ID, "com.esri.earth.phone:id/et_search")
        search_input.send_keys("Esri")
        time.sleep(mid_sleep)
        first_input = self.driver.find_element(app.XPATH,
                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView")
        first_input.click()
        time.sleep(mid_sleep)
        placemark = self.driver.find_element(app.ID, "com.esri.earth.phone:id/image_add_favourt")
        placemark.click()
        route = self.driver.find_element(app.ID, "com.esri.earth.phone:id/image_route")
        route.click()
        google_maps = self.driver.find_element(app.ID, "com.esri.earth.phone:id/cl_item")
        google_maps.click()

        # back button
        # self.driver.press_keycode(3)

        # recents button
        self.driver.press_keycode(187)
        self.driver.press_keycode(187)

        close = self.driver.find_element(app.ID, "com.esri.earth.phone:id/img_close_search")
        close.click()

    def test_7_full_screen(self):
        full_screen = self.driver.find_element(app.ID, "com.esri.earth.phone:id/rl_full_screen")
        full_screen.click()
        time.sleep(lil_sleep)
        self.driver.swipe(self.middle_of_screen, self.middle_of_screen, self.middle_of_screen, self.middle_of_screen, 1)

    def test_8_share_function(self):
        share = self.driver.find_element(app.ID, "com.esri.earth.phone:id/rl_screenshot")
        share.click()
        time.sleep(mid_sleep)
        self.driver.press_keycode(3)

    # move = self.driver.find_element(app.XPATH,
    #                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
    # move.click()

    # add = self.driver.find_element(app.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView")
    # add.click()
    # portal = self.driver.find_element(app.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
    # portal.click()


if __name__ == '__main__':
    unittest.main()
