from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that
from base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):

    def test_valid_signin_process(self):
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/login").click()
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/email").send_keys("dharapurohit@123.com")
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/password").send_keys("dhara123")
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/create_account").click()
       