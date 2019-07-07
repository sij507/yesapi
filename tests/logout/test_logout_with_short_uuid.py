import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Logout Request')
class TestLogoutWithShortUuid:
    admin_token = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up admin login params'):
            params = Params.setup_login_params(
                constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)

        with allure.step("send an admin login request"):
            manager_success_login = SendRequest(constants.GET, constants.BASE_URL,
                                                params)

        with allure.step("Get admin token"):
            TestLogoutWithShortUuid.admin_token = manager_success_login.get_token()

    def test_log_out_with_admin_success(self):
        with allure.step('Set up admin logout params'):
            params = Params.setup_logout_params(constants.SHORT_UUID, TestLogoutWithShortUuid.admin_token,
                                                constants.APP_KEY)

        with allure.step("Send an admin logout request"):
            manager_logout_with_short_uuid = SendRequest(constants.GET, constants.BASE_URL, params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(manager_logout_with_short_uuid.get_ret()), "Actual:")
            assert manager_logout_with_short_uuid.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGOUT_SHORT_UUID, "Expected:")
            allure.attach("Msg: " + manager_logout_with_short_uuid.get_msg(), "Actual:")
            assert manager_logout_with_short_uuid.get_msg() == constants.ERR_MSG_LOGOUT_SHORT_UUID