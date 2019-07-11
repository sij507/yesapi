import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.logout import Logout


@allure.feature('Login Request')
class TestLogoutWithoutAppKey:

    def test_logout_without_app_key(self):
        with allure.step('Send logout request without app key'):
            logout_without_app_key = SendRequest(
                Logout.get_test_case("test_logout_without_app_key",  constants.TMP_TOKEN))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_APP_KEY, "Expected:")
            allure.attach("Msg: " + logout_without_app_key.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_APP_KEY in logout_without_app_key.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(logout_without_app_key.get_ret()), "Actual:")
            assert logout_without_app_key.get_ret() == constants.RET_400
