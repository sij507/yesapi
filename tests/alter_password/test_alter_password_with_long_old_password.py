import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithLongOldPassword:

    def test_alter_password_with_long_old_password(self):
        with allure.step('Send alter password request with long old password'):
            alter_password_long_old_password = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_long_old_password"))

        with allure.step("Checking msg"):
            allure.attach("Msg contains: " + constants.ERR_MSG_OLD_PASSWORD_TOO_LONG, "Expected")
            allure.attach("Msg: " + alter_password_long_old_password.get_msg(), "Actual:")
            assert constants.ERR_MSG_OLD_PASSWORD_TOO_LONG in alter_password_long_old_password.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_long_old_password.get_ret()), "Actual:")
            assert alter_password_long_old_password.get_ret() == constants.RET_400