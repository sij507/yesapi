import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Check User Status Request')
class TestCheckUserStatusShortUuid:

    def test_user_status_not_logged_in(self):
        with allure.step("Send check user status request with short uuid"):
            check_login_status_with_short_uuid = SendRequest(
                CheckUserStatus.get_test_case("test_check_user_status_with_short_uuid"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(check_login_status_with_short_uuid.get_ret()), "Actual:")
            assert check_login_status_with_short_uuid.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_CHECK_SHORT_UUID, "Expected")
            allure.attach("Msg: " + check_login_status_with_short_uuid.get_msg(), "Actual:")
            assert check_login_status_with_short_uuid.get_msg() == constants.ERR_MSG_CHECK_SHORT_UUID
