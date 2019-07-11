import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.login import Login


@allure.feature('Login Request')
class TestLoginwithRegularUserSuccess:

    def test_login_with_regular_user_success(self):
        with allure.step('Send a valid regular user login request'):
            login_with_regular_user_success = SendRequest(Login.get_test_case("test_login_with_regular_user_success"))

        with allure.step('Checking Uuid'):
            allure.attach("Uuid: " + constants.USER_UUID, "Expected:")
            allure.attach("Uuid: " + login_with_regular_user_success.get_uuid(), "Actual:")
            assert login_with_regular_user_success.get_uuid() == constants.USER_UUID

        with allure.step('Checking role'):
            allure.attach("Role: " + constants.ROLE_USER, "Expected:")
            allure.attach("Role: " + login_with_regular_user_success.get_role(), "Actual:")
            assert login_with_regular_user_success.get_role() == constants.ROLE_USER

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(login_with_regular_user_success.get_ret()), "Actual:")
            assert login_with_regular_user_success.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(login_with_regular_user_success.get_err_code()), "Actual:")
            assert login_with_regular_user_success.get_err_code() == constants.ERR_CODE_0
