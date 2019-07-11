import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithoutOldPassword:

    def test_alter_password_without_old_password(self):
        with allure.step('Send alter password request without old password'):
            alter_password_without_old_password = SendRequest(
                AlterPassword.get_test_case("test_alter_password_without_old_password"))

        with allure.step("Checking msg"):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_OLD_PASSWORD, "Expected")
            allure.attach("Msg: " + alter_password_without_old_password.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_OLD_PASSWORD in alter_password_without_old_password.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_without_old_password.get_ret()), "Actual:")
            assert alter_password_without_old_password.get_ret() == constants.RET_400
