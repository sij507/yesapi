import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Login Request')
class TestCheckUserStatusWrongAppKey:

    def test_check_user_status_with_wrong_app_key(self):
        with allure.step('Send an admin login request with wrong app key'):
            check_user_status_with_wrong_app_key = SendRequest(CheckUserStatus.get_test_case("test_check_user_status_with_wrong_app_key"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_406), "Expected:")
            allure.attach("Ret: " + str(check_user_status_with_wrong_app_key.get_ret()), "Actual:")
            assert check_user_status_with_wrong_app_key.get_ret() == constants.RET_406

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_CHECK_WRONG_APP_KEY, "Expected:")
            allure.attach("Msg: " + check_user_status_with_wrong_app_key.get_msg(), "Actual:")
            assert check_user_status_with_wrong_app_key.get_msg() == constants.ERR_MSG_CHECK_WRONG_APP_KEY
