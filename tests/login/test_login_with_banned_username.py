import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithBannedUsername:

    def test_login_with_banned_username(self):
        with allure.step('Send a login request with banned username'):
            login_with_banned_username = SendRequest(Login.get_test_case("test_login_with_banned_username"))

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg contains: " + constants.ERR_MSG_WRONG_PASSWORD_OR_BANNED_USERNAME, "Expected:")
            allure.attach("Err_msg: " + login_with_banned_username.get_err_msg(), "Actual:")
            assert constants.ERR_MSG_WRONG_PASSWORD_OR_BANNED_USERNAME in login_with_banned_username.get_err_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(login_with_banned_username.get_ret()), "Actual:")
            assert login_with_banned_username.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_2), "Expected:")
            allure.attach("Err_code: " + str(login_with_banned_username.get_err_code()), "Actual:")
            assert login_with_banned_username.get_err_code() == constants.ERR_CODE_2

