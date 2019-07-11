import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.alter_password import AlterPassword


@allure.feature('Login Request')
class TestAlterPasswordWithWrongAppKey:

    def test_login_with_wrong_app_key(self):
        with allure.step('Send alter password request with wrong app key'):
            alter_password_with_wrong_app_key = SendRequest(
                AlterPassword.get_test_case("test_alter_password_with_wrong_app_key"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_WRONG_APP_KEY, "Expected:")
            allure.attach("Msg: " + alter_password_with_wrong_app_key.get_msg(), "Actual:")
            assert constants.ERR_MSG_WRONG_APP_KEY in alter_password_with_wrong_app_key.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_406), "Expected:")
            allure.attach("Ret: " + str(alter_password_with_wrong_app_key.get_ret()), "Actual:")
            assert alter_password_with_wrong_app_key.get_ret() == constants.RET_406
