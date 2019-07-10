import allure
from data import constants
import pytest
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus
from data.test_cases.login import Login


@allure.feature('Check User Status Request')
class TestAdminStatusLoggedIn:
    admin_token = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step("Send an admin login request"):
            admin_success_login = SendRequest(Login.get_test_case("test_login_with_admin_success"))

        with allure.step("Get admin login token"):
            TestAdminStatusLoggedIn.admin_token = admin_success_login.get_token()

    def test_check_admin_status_logged_in(self):
        with allure.step("Send check admin status request(logged in)"):
            check_login_status_logged_in = SendRequest(
                CheckUserStatus.get_test_case("test_check_admin_status_logged_in", TestAdminStatusLoggedIn.admin_token))

        print(check_login_status_logged_in.get_response())
        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(check_login_status_logged_in.get_ret()), "Actual:")
            assert check_login_status_logged_in.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(check_login_status_logged_in.get_err_code()), "Actual:")
            assert check_login_status_logged_in.get_err_code() == constants.ERR_CODE_0
