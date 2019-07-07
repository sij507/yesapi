import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Login Request')
class TestLoginWithLongPassword:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up admin login params'):
            TestLoginWithLongPassword.params = Params.setup_login_params(
                constants.ADMIN_USERNAME, constants.LONG_MD5_PASSWORD, constants.APP_KEY)

    def test_login_with_long_password(self):
        with allure.step('Send a login request with long password'):
            invalid_long_password_login = SendRequest(constants.GET, constants.BASE_URL, TestLoginWithLongPassword.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(invalid_long_password_login.get_ret()), "Actual:")
            assert invalid_long_password_login.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGIN_PASSWORD_TOO_LONG, "Expected:")
            allure.attach("Msg: " + invalid_long_password_login.get_msg(), "Actual:")
            assert invalid_long_password_login.get_msg() == constants.ERR_MSG_LOGIN_PASSWORD_TOO_LONG