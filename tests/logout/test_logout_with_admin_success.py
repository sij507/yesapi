import allure
from data import constants
import pytest
from request.send_request import SendRequest
from data.test_cases.logout import Logout
from data.test_cases.login import Login


@allure.feature('Logout Request')
class TestLogOutWithAdminSuccess:
    admin_token = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step("send an admin login request"):
            admin_success_login = SendRequest(
                Login.get_test_case("test_login_with_admin_success"))

        with allure.step("Get admin token"):
            TestLogOutWithAdminSuccess.admin_token = admin_success_login.get_token()

    def test_logout_with_admin_success(self):
        with allure.step("Send an admin logout request"):
            admin_success_logout = SendRequest(Logout.get_test_case(
                "test_logout_with_admin_success", TestLogOutWithAdminSuccess.admin_token))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(admin_success_logout.get_ret()), "Actual:")
            assert admin_success_logout.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(admin_success_logout.get_err_code()), "Actual:")
            assert admin_success_logout.get_err_code() == constants.ERR_CODE_0
