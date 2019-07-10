import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithShortAppKey:

    def test_login_with_short_app_key(self):
        with allure.step('Send an admin login request with short app key'):
            login_with_short_app_key = SendRequest(Login.get_test_case("test_login_with_short_app_key"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(login_with_short_app_key.get_ret()), "Actual:")
            assert login_with_short_app_key.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGIN_SHORT_APP_KEY, "Expected:")
            allure.attach("Msg: " + login_with_short_app_key.get_msg(), "Actual:")
            assert login_with_short_app_key.get_msg() == constants.ERR_MSG_LOGIN_SHORT_APP_KEY