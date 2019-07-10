import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Check User Status Request')
class TestCheckUserStatusWithWrongUuid:

    def test_user_status_with_wrong_token(self):
        with allure.step("Send check user status request with wrong uuid"):
            check_login_status_with_wrong_uuid = SendRequest(
                CheckUserStatus.get_test_case("test_check_user_status_with_wrong_uuid"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(check_login_status_with_wrong_uuid.get_ret()), "Actual:")
            assert check_login_status_with_wrong_uuid.get_ret() == constants.RET_200

        with allure.step("Checking err msg"):
            allure.attach("Err msg: " + constants.ERR_MSG_CHECK_WRONG_TOKEN_OR_UUID, "Expected")
            allure.attach("Err msg: " + check_login_status_with_wrong_uuid.get_err_msg(), "Actual:")
            assert check_login_status_with_wrong_uuid.get_err_msg() == constants.ERR_MSG_CHECK_WRONG_TOKEN_OR_UUID