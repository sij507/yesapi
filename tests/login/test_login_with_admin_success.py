import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Login Request')
class TestLoginWithAdminSuccess:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up admin login params'):
            TestLoginWithAdminSuccess.params = Params.setup_login_params(
                constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)

    def test_login_with_admin_success(self):
        with allure.step('Send a valid admin login request'):
            manager_success_login = SendRequest(constants.GET, constants.BASE_URL, TestLoginWithAdminSuccess.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(manager_success_login.get_ret()), "Actual:")
            assert manager_success_login.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(manager_success_login.get_err_code()), "Actual:")
            assert manager_success_login.get_err_code() == constants.ERR_CODE_0

        with allure.step('Checking uuid'):
            allure.attach("Uuid: " + constants.ADMIN_UUID, "Expected:")
            allure.attach("Uuid: " + manager_success_login.get_uuid(), "Actual:")
            assert manager_success_login.get_uuid() == constants.ADMIN_UUID

        with allure.step('Checking role'):
            allure.attach("Role: " + constants.ROLE_ADMIN, "Expected:")
            allure.attach("Role: " + manager_success_login.get_role(), "Actual:")
            assert manager_success_login.get_role() == constants.ROLE_ADMIN
