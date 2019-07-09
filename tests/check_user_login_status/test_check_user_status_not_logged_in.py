import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.check_user_status import CheckUserStatus


@allure.feature('Check User Status Request')
class TestUserStatusNotLoggedIn:

    def test_user_status_not_logged_in(self):
        with allure.step("Send an user login request(not logged in"):
            check_login_status_not_logged_in = SendRequest(
                CheckUserStatus.get_test_case("test_check_user_status_not_logged_in"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(check_login_status_not_logged_in.get_ret()), "Actual:")
            assert check_login_status_not_logged_in.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_1), "Expected:")
            allure.attach("Err_code: " + str(check_login_status_not_logged_in.get_err_code()), "Actual:")
            assert check_login_status_not_logged_in.get_err_code() == constants.ERR_CODE_1
