import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithInvalidUsername:

    def test_login_with_invalid_username(self):
        with allure.step('Send a login request with invalid username'):
            invalid_username_login = SendRequest(Login.get_test_case("test_login_with_invalid_username"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(invalid_username_login.get_ret()), "Actual:")
            assert invalid_username_login.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_1), "Expected:")
            allure.attach("Err_code: " + str(invalid_username_login.get_err_code()), "Actual:")
            assert invalid_username_login.get_err_code() == constants.ERR_CODE_1

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg " + constants.ERR_MSG_LOGIN_FAILED, "Expected:")
            allure.attach("Err_msg: " + invalid_username_login.get_err_msg(), "Actual:")
            assert invalid_username_login.get_err_msg() == constants.ERR_MSG_LOGIN_FAILED
