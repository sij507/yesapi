import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithWrongOldPassword:

    def test_alter_password_with_wrong_old_password(self):
        with allure.step('Send alter password request with wrong old password'):
            alter_password_with_wrong_old_password = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_wrong_old_password"))

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg contains: " + constants.ERR_MSG_WRONG_PASSWORD_OR_USERNAME, "Expected:")
            allure.attach("Err_msg: " + alter_password_with_wrong_old_password.get_err_msg(), "Actual:")
            assert constants.ERR_MSG_WRONG_PASSWORD_OR_USERNAME in alter_password_with_wrong_old_password.get_err_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(alter_password_with_wrong_old_password.get_ret()), "Actual:")
            assert alter_password_with_wrong_old_password.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_1), "Expected:")
            allure.attach("Err_code: " + str(alter_password_with_wrong_old_password.get_err_code()), "Actual:")
            assert alter_password_with_wrong_old_password.get_err_code() == constants.ERR_CODE_1