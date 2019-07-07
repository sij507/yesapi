import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import  Params


@allure.feature('Alter Password Request')
class TestAlterPasswordSuccess:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up alter password params'):
            TestAlterPasswordSuccess.params = Params.setup_alter_password_params(
                constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD,
                constants.APP_KEY)
        yield
        with allure.step('Set up alter password params'):
            TestAlterPasswordSuccess.params = Params.setup_alter_password_params(
                constants.REGULAR_USERNAME, constants.NEW_PASSWORD, constants.MD5_PASSWORD,
                constants.APP_KEY)
        with allure.step('Reset back the password'):
            SendRequest(constants.GET, constants.BASE_URL, TestAlterPasswordSuccess.params)

    @pytest.mark.alter_password
    def test_alter_password_success(self):
        with allure.step('Send an alter password success request'):
            alter_password_success = SendRequest(constants.GET, constants.BASE_URL,
                                                 TestAlterPasswordSuccess.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(alter_password_success.get_ret()), "Actual:")
            assert alter_password_success.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(alter_password_success.get_err_code()), "Actual:")
            assert alter_password_success.get_err_code() == constants.ERR_CODE_0

        with allure.step('Set up user login params'):
            success_login_params = Params.setup_login_params(constants.REGULAR_USERNAME, constants.NEW_PASSWORD,
                                                             constants.APP_KEY)
        with allure.step('Checking if the user can log in with new password'):
            success_login = SendRequest(constants.GET, constants.BASE_URL, success_login_params)
            allure.attach("Ret = " + str(constants.RET_200) +
                          "and Err_code = " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Ret = " + str(constants.ERR_CODE_0) +
                          "Err_code =  " + str(alter_password_success.get_err_code()), "Actual:")
            assert success_login.get_ret() == constants.RET_200
            assert success_login.get_err_code() == constants.ERR_CODE_0

