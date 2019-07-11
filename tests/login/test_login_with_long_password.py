import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithLongPassword:

    def test_login_with_long_password(self):
        with allure.step('Send a login request with long password'):
            login_with_long_password = SendRequest(Login.get_test_case("test_login_with_long_password"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_LONG_PASSWORD, "Expected:")
            allure.attach("Msg: " + login_with_long_password.get_msg(), "Actual:")
            assert constants.ERR_MSG_LONG_PASSWORD in login_with_long_password.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(login_with_long_password.get_ret()), "Actual:")
            assert login_with_long_password.get_ret() == constants.RET_400