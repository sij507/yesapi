import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithShortOldPassword:

    def test_alter_password_with_short_old_password(self):
        with allure.step('Send alter password request with short old password'):
            alter_password_with_short_old_password = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_short_old_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_with_short_old_password.get_ret()), "Actual:")
            assert alter_password_with_short_old_password.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_ALTER_PSW_OLD_PASSWORD_TOO_SHORT, "Expected")
            allure.attach("Msg: " + alter_password_with_short_old_password.get_msg(), "Actual:")
            assert alter_password_with_short_old_password.get_msg() == constants.ERR_MSG_ALTER_PSW_OLD_PASSWORD_TOO_SHORT
