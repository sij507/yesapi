import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithShortPassword:

    def test_alter_password_with_short_password(self):
        with allure.step('Send an alter password request with short password'):
            alter_password_wrong_username = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_short_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_wrong_username.get_ret()), "Actual:")
            assert alter_password_wrong_username.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_ALTER_PSW_PASSWORD_TOO_SHORT, "Expected")
            allure.attach("Msg: " + alter_password_wrong_username.get_msg(), "Actual:")
            assert alter_password_wrong_username.get_msg() == constants.ERR_MSG_ALTER_PSW_PASSWORD_TOO_SHORT
