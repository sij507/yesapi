import allure
from data import constants
import pytest
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword
from data.test_cases.login import Login


@allure.feature('Alter Password Request')
class TestAlterPasswordSuccess:

    @pytest.fixture(autouse=True)
    def set_up(self):
        yield
        with allure.step('Reset back the password'):
            SendRequest(AlterPassword.get_test_case("test_alter_password_reset_back_password"))

    def test_alter_password_success(self):
        with allure.step('Send alter password request(success)'):
            alter_password_success = SendRequest(AlterPassword.get_test_case("test_alter_password_success"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(alter_password_success.get_ret()), "Actual:")
            assert alter_password_success.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(alter_password_success.get_err_code()), "Actual:")
            assert alter_password_success.get_err_code() == constants.ERR_CODE_0

        with allure.step('Checking if the user can log in with new password'):
            login_with_new_password = SendRequest(Login.get_test_case("test_login_with_new_password"))

            allure.attach("Ret = " + str(constants.RET_200) +
                          "and Err_code = " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Ret = " + str(constants.ERR_CODE_0) +
                          "Err_code =  " + str(alter_password_success.get_err_code()), "Actual:")
            assert login_with_new_password.get_ret() == constants.RET_200
            assert login_with_new_password.get_err_code() == constants.ERR_CODE_0

