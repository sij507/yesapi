import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithLongPassword:

    def test_login_with_long_password(self):
        with allure.step('Send a login request with long password'):
            invalid_long_password_login = SendRequest(Login.get_test_case("test_login_with_long_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(invalid_long_password_login.get_ret()), "Actual:")
            assert invalid_long_password_login.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGIN_PASSWORD_TOO_LONG, "Expected:")
            allure.attach("Msg: " + invalid_long_password_login.get_msg(), "Actual:")
            assert invalid_long_password_login.get_msg() == constants.ERR_MSG_LOGIN_PASSWORD_TOO_LONG