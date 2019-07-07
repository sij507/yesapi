import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Alter Password Request')
class TestAlterPasswordWithShortPassword:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up alter password params'):
            TestAlterPasswordWithShortPassword.params = Params.setup_alter_password_params(
                constants.REGULAR_USERNAME, constants.SHORT_MD5_PASSWORD, constants.NEW_PASSWORD, constants.APP_KEY)

    def test_alter_password_with_short_password(self):
        with allure.step('Send an alter password request with short password'):
            alter_password_wrong_username = SendRequest(constants.GET, constants.BASE_URL,
                                                        TestAlterPasswordWithShortPassword.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_wrong_username.get_ret()), "Actual:")
            assert alter_password_wrong_username.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_ALTER_PSW_PASSWORD_TOO_SHORT, "Expected")
            allure.attach("Msg: " + alter_password_wrong_username.get_msg(), "Actual:")
            assert alter_password_wrong_username.get_msg() == constants.ERR_MSG_ALTER_PSW_PASSWORD_TOO_SHORT
