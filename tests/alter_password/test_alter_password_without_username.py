import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.alter_password import AlterPassword


@allure.feature('Alter Password Request')
class TestAlterPasswordWithoutUsername:

    def test_alter_password_without_username(self):
        with allure.step('Send alter password request without username'):
            alter_password_without_username = SendRequest(
                AlterPassword.get_test_case("test_alter_password_without_username"))

        with allure.step("Checking msg"):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_USERNAME, "Expected")
            allure.attach("Msg: " + alter_password_without_username.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_USERNAME in alter_password_without_username.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(alter_password_without_username.get_ret()), "Actual:")
            assert alter_password_without_username.get_ret() == constants.RET_400
