import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithoutUsername:

    def test_login_without_username(self):
        with allure.step('Send an admin login request without username'):
            login_without_username = SendRequest(Login.get_test_case("test_login_without_username"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(login_without_username.get_ret()), "Actual:")
            assert login_without_username.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGIN_WITHOUT_USERNAME, "Expected:")
            allure.attach("Msg: " + login_without_username.get_msg(), "Actual:")
            assert login_without_username.get_msg() == constants.ERR_MSG_LOGIN_WITHOUT_USERNAME