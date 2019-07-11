import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithoutAppKey:

    def test_alter_password_without_app_key(self):
        with allure.step('Send alter password request without app key'):
            alter_password_without_app_key = SendRequest(
                AlterPassword.get_test_case("test_alter_password_without_app_key"))

        with allure.step("Checking msg"):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_APP_KEY, "Expected")
            allure.attach("Msg: " + alter_password_without_app_key.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_APP_KEY in alter_password_without_app_key.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_without_app_key.get_ret()), "Actual:")
            assert alter_password_without_app_key.get_ret() == constants.RET_400
