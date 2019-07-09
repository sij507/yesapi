import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginWithAdminSuccess:

    def test_login_with_admin_success(self):
        with allure.step('Send a valid admin login request'):
            admin_success_login = SendRequest(Login.get_test_case("test_login_with_admin_success"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(admin_success_login.get_ret()), "Actual:")
            assert admin_success_login.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(admin_success_login.get_err_code()), "Actual:")
            assert admin_success_login.get_err_code() == constants.ERR_CODE_0

        with allure.step('Checking uuid'):
            allure.attach("Uuid: " + constants.ADMIN_UUID, "Expected:")
            allure.attach("Uuid: " + admin_success_login.get_uuid(), "Actual:")
            assert admin_success_login.get_uuid() == constants.ADMIN_UUID

        with allure.step('Checking role'):
            allure.attach("Role: " + constants.ROLE_ADMIN, "Expected:")
            allure.attach("Role: " + admin_success_login.get_role(), "Actual:")
            assert admin_success_login.get_role() == constants.ROLE_ADMIN
