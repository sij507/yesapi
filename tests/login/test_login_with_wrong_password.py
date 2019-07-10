import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithWrongPassword:

    def test_login_with_wrong_password(self):
        with allure.step('Send a login request with wrong password'):
            login_with_wrong_password = SendRequest(Login.get_test_case("test_login_with_wrong_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(login_with_wrong_password.get_ret()), "Actual:")
            assert login_with_wrong_password.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_2), "Expected:")
            allure.attach("Err_code: " + str(login_with_wrong_password.get_err_code()), "Actual:")
            assert login_with_wrong_password.get_err_code() == constants.ERR_CODE_2

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg " + constants.ERR_MSG_LOGIN_WRONG_PASSWORD_OR_BANNED_USERNAME, "Expected:")
            allure.attach("Err_msg: " + login_with_wrong_password.get_err_msg(), "Actual:")
            assert login_with_wrong_password.get_err_msg() == constants.ERR_MSG_LOGIN_WRONG_PASSWORD_OR_BANNED_USERNAME

