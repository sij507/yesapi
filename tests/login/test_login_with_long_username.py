import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithLongUsername:

    def test_login_with_long_username(self):
        with allure.step('Send a login request with long username'):
            login_with_long_username = SendRequest(Login.get_test_case("test_login_with_long_username"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_LONG_USERNAME, "Expected:")
            allure.attach("Msg: " + login_with_long_username.get_msg(), "Actual:")
            assert constants.ERR_MSG_LONG_USERNAME in login_with_long_username.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(login_with_long_username.get_ret()), "Actual:")
            assert login_with_long_username.get_ret() == constants.RET_400
