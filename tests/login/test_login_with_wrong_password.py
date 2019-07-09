import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithWrongPassword:

    def test_login_with_wrong_password(self):
        with allure.step('Send a login request with wrong password'):
            wrong_password_login = SendRequest(Login.get_test_case("test_login_with_wrong_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(wrong_password_login.get_ret()), "Actual:")
            assert wrong_password_login.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_2), "Expected:")
            allure.attach("Err_code: " + str(wrong_password_login.get_err_code()), "Actual:")
            assert wrong_password_login.get_err_code() == constants.ERR_CODE_2

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg " + constants.ERR_MSG_LOGIN_WRONG_PASSWORD_OR_USERNAME, "Expected:")
            allure.attach("Err_msg: " + wrong_password_login.get_err_msg(), "Actual:")
            assert wrong_password_login.get_err_msg() == constants.ERR_MSG_LOGIN_WRONG_PASSWORD_OR_USERNAME

