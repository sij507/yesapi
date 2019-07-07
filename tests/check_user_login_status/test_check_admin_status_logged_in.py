import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Check User Status Request')
class TestAdminStatusLoggedIn:
    admin_token = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up admin login params'):
            admin_login_params = Params.setup_login_params(constants.ADMIN_USERNAME,
                                                           constants.MD5_PASSWORD, constants.APP_KEY)
        with allure.step("Send an admin login status request(logged in)"):
            admin_success_login = SendRequest(constants.GET, constants.BASE_URL, admin_login_params)

        with allure.step("Get admin login token"):
            TestAdminStatusLoggedIn.admin_token = admin_success_login.get_token()

    def test_admin_status_logged_in(self):
        with allure.step("Set up check admin status login params"):
            params = Params.setup_check_params(constants.ADMIN_UUID, TestAdminStatusLoggedIn.admin_token,
                                               constants.APP_KEY)

        with allure.step("Send a check admin user status request"):
            check_login_status_logged_in = SendRequest(constants.GET, constants.BASE_URL, params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(check_login_status_logged_in.get_ret()), "Actual:")
            assert check_login_status_logged_in.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(check_login_status_logged_in.get_err_code()), "Actual:")
            assert check_login_status_logged_in.get_err_code() == constants.ERR_CODE_0
