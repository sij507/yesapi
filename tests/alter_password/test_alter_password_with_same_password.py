import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Alter Password Request')
class TestAlterPasswordWithSamePassword:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up alter password params'):
            TestAlterPasswordWithSamePassword.params = Params.setup_alter_password_params(
                constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.MD5_PASSWORD, constants.APP_KEY)

    def test_alter_password_with_same_password(self):
        with allure.step('Send an alter password request with same password'):
            alter_password_same_password = SendRequest(constants.GET, constants.BASE_URL,
                                                       TestAlterPasswordWithSamePassword.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(alter_password_same_password.get_ret()), "Actual:")
            assert alter_password_same_password.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_2), "Expected:")
            allure.attach("Err_code: " + str(alter_password_same_password.get_err_code()), "Actual:")
            assert alter_password_same_password.get_err_code() == constants.ERR_CODE_2

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg " + constants.ERR_MSG_ALTER_PSW_WRONG_PASSWORD_OR_USERNAME, "Expected:")
            allure.attach("Err_msg: " + alter_password_same_password.get_err_msg(), "Actual:")
            assert alter_password_same_password.get_err_msg() == constants.ERR_MSG_ALTER_PSW_PASSWORD_SAME_PASSWORD

