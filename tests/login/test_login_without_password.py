import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithoutPassword:

    def test_login_without_password(self):
        with allure.step('Send an admin login request without password'):
            login_without_password = SendRequest(Login.get_test_case("test_login_without_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(login_without_password.get_ret()), "Actual:")
            assert login_without_password.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGIN_WITHOUT_PASSWORD, "Expected:")
            allure.attach("Msg: " + login_without_password.get_msg(), "Actual:")
            assert login_without_password.get_msg() == constants.ERR_MSG_LOGIN_WITHOUT_PASSWORD