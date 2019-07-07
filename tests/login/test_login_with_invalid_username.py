import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Login Request')
class TestLoginWithInvalidUsername:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up admin login params'):
            TestLoginWithInvalidUsername.params = Params.setup_login_params(
                constants.WRONG_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)

    def test_login_with_invalid_username(self):
        with allure.step('Send a login request with invalid username'):
            invalid_username_login = SendRequest(constants.GET, constants.BASE_URL,
                                                 TestLoginWithInvalidUsername.params)

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
