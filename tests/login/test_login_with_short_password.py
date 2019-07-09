import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithShortPassword:

    def test_login_with_short_password(self):
        with allure.step('Send a login request with short password'):
            invalid_short_password_login = SendRequest(Login.get_test_case("test_login_with_short_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(invalid_short_password_login.get_ret()), "Actual:")
            assert invalid_short_password_login.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGIN_PASSWORD_TOO_SHORT, "Expected:")
            allure.attach("Msg: " + invalid_short_password_login.get_msg(), "Actual:")
            assert invalid_short_password_login.get_msg() == constants.ERR_MSG_LOGIN_PASSWORD_TOO_SHORT