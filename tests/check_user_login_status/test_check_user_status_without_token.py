import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Check User Status Request')
class TestCheckUserStatusWithoutToken:

    def test_check_user_status_without_token(self):
        with allure.step("Send check user status request without token"):
            check_user_status_without_token = SendRequest(
                CheckUserStatus.get_test_case("test_check_user_status_without_token"))

        with allure.step("Checking msg"):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_TOKEN, "Expected")
            allure.attach("Msg: " + check_user_status_without_token.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_TOKEN in check_user_status_without_token.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(check_user_status_without_token.get_ret()), "Actual:")
            assert check_user_status_without_token.get_ret() == constants.RET_400