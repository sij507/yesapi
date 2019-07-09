import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginwithRegularUserSuccess:

    def test_login_with_regular_user_success(self):
        with allure.step('Send a valid regular user login request'):
            user_success_login = SendRequest(Login.get_test_case("test_login_with_regular_user_success"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(user_success_login.get_ret()), "Actual:")
            assert user_success_login.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(user_success_login.get_err_code()), "Actual:")
            assert user_success_login.get_err_code() == constants.ERR_CODE_0

        with allure.step('Checking Err_code'):
            allure.attach("Uuid: " + constants.USER_UUID, "Expected:")
            allure.attach("Uuid: " + user_success_login.get_uuid(), "Actual:")
            assert user_success_login.get_uuid() == constants.USER_UUID

        with allure.step('Checking role'):
            allure.attach("Role: " + constants.ROLE_USER, "Expected:")
            allure.attach("Role: " + user_success_login.get_role(), "Actual:")
            assert user_success_login.get_role() == constants.ROLE_USER
