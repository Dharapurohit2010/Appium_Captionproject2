import pytest
from appium import webdriver
from utilities import read_utils


class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic = read_utils.get_value_from_json("../testdata/config.json", "device")
        json_dic_port = read_utils.get_value_from_json("../testdata/config.json", "port")
        if json_dic == "local":
            des_cap = {
                "platformName": "Android",
                "deviceName": "oneplus",
                "app": r"org_coursera_android_v4.3.0.apk",
                # "noReset": True,
            }
        else:
            des_cap = {
                "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Behave Android Project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "dharapurohit_HAN9ix",
                    "accessKey": "geskDsFgcMWnAWRTqEEc"
                }
            }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()
x