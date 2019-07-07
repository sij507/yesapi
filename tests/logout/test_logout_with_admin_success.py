import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Logout Request')
class TestLogOutWithAdminSuccess:
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
            TestLogOutWithAdminSuccess.admin_token = manager_success_login.get_token()

    def test_log_out_with_admin_success(self):
        with allure.step('Set up admin logout params'):
            params = Params.setup_logout_params(constants.ADMIN_UUID, TestLogOutWithAdminSuccess.admin_token,
                                                constants.APP_KEY)

        with allure.step("Send an admin logout request"):
            manager_success_logout = SendRequest(constants.GET, constants.BASE_URL, params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(manager_success_logout.get_ret()), "Actual:")
            assert manager_success_logout.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(manager_success_logout.get_err_code()), "Actual:")
            assert manager_success_logout.get_err_code() == constants.ERR_CODE_0
