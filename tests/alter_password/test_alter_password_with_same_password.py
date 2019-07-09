import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithSamePassword:
    def test_alter_password_with_same_password(self):
        with allure.step('Send an alter password request with same password'):
            alter_password_same_password = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_same_password"))

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

