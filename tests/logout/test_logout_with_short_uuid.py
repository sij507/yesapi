import allure
from data import constants
import pytest
from request.send_request import SendRequest
from data.test_cases.logout import Logout
from data.test_cases.login import Login


@allure.feature('Logout Request')
class TestLogoutWithShortUuid:
    admin_token = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step("send an admin login request"):
            manager_success_login = SendRequest(Login.get_test_case("test_login_with_admin_success"))

        with allure.step("Get admin token"):
            TestLogoutWithShortUuid.admin_token = manager_success_login.get_token()

    def test_log_out_with_admin_success(self):
        with allure.step("Send an admin logout request"):
            manager_logout_with_short_uuid = SendRequest(Logout.get_test_case(
                "test_logout_with_short_uuid", TestLogoutWithShortUuid.admin_token))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(manager_logout_with_short_uuid.get_ret()), "Actual:")
            assert manager_logout_with_short_uuid.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGOUT_SHORT_UUID, "Expected:")
            allure.attach("Msg: " + manager_logout_with_short_uuid.get_msg(), "Actual:")
            assert manager_logout_with_short_uuid.get_msg() == constants.ERR_MSG_LOGOUT_SHORT_UUID