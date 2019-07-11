import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Check User Status Request')
class TestCheckUserStatusWithoutUuid:

    def test_check_user_status_without_uuid(self):
        with allure.step("Send check user status request without uuid"):
            check_user_status_without_uuid = SendRequest(
                CheckUserStatus.get_test_case("test_check_user_status_without_uuid"))

        with allure.step("Checking msg"):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_UUID, "Expected")
            allure.attach("Msg: " + check_user_status_without_uuid.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_UUID in check_user_status_without_uuid.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(check_user_status_without_uuid.get_ret()), "Actual:")
            assert check_user_status_without_uuid.get_ret() == constants.RET_400