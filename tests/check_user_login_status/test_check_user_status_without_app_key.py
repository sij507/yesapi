import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Check User Status Request')
class TestCheckUserStatusWithoutAppKey:

    def test_user_status_without_app_key(self):
        with allure.step("Send check user status request without app key"):
            check_login_status_without_app_key = SendRequest(
                CheckUserStatus.get_test_case("test_check_user_status_without_app_key"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(check_login_status_without_app_key.get_ret()), "Actual:")
            assert check_login_status_without_app_key.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_CHECK_WITHOUT_APP_KEY, "Expected")
            allure.attach("Msg: " + check_login_status_without_app_key.get_msg(), "Actual:")
            assert check_login_status_without_app_key.get_msg() == constants.ERR_MSG_CHECK_WITHOUT_APP_KEY