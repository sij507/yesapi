import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithNonexistentUsername:

    def test_alter_password_with_nonexistent_username(self):
        with allure.step('Send alter password request with nonexistent username'):
            alter_password_invalid_username = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_nonexistent_username"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(alter_password_invalid_username.get_ret()), "Actual:")
            assert alter_password_invalid_username.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_1), "Expected:")
            allure.attach("Err_code: " + str(alter_password_invalid_username.get_err_code()), "Actual:")
            assert alter_password_invalid_username.get_err_code() == constants.ERR_CODE_1

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg " + constants.ERR_MSG_ALTER_PSW_WRONG_PASSWORD_OR_USERNAME, "Expected:")
            allure.attach("Err_msg: " + alter_password_invalid_username.get_err_msg(), "Actual:")
            assert alter_password_invalid_username.get_err_msg() == constants.ERR_MSG_ALTER_PSW_WRONG_PASSWORD_OR_USERNAME