import allure
from data import constants
import pytest
from request.send_request import SendRequest
from data.test_cases.logout import Logout
from data.test_cases.login import Login


@allure.feature('Logout Request')
class TestLogoutWithLongUuid:

    def test_log_out_with_admin_success(self):
        with allure.step("Send an admin logout request"):
            manager_logout_with_long_uuid = SendRequest(
                Logout.get_test_case("test_logout_with_long_uuid", constants.TMP_TOKEN))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(manager_logout_with_long_uuid.get_ret()), "Actual:")
            assert manager_logout_with_long_uuid.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGOUT_LONG_UUID, "Expected:")
            allure.attach("Msg: " + manager_logout_with_long_uuid.get_msg(), "Actual:")
            assert manager_logout_with_long_uuid.get_msg() == constants.ERR_MSG_LOGOUT_LONG_UUID