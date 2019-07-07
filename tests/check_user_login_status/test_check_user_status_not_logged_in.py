import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Check User Status Request')
class TestUserStatusNotLoggedIn:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up check user login params'):
            TestUserStatusNotLoggedIn.params = Params.setup_check_params(
                constants.USER_UUID, constants.TMP_TOKEN, constants.APP_KEY)

    def test_user_status_not_logged_in(self):
        with allure.step("Send an user login request(not logged in"):
            check_login_status_not_logged_in = SendRequest(constants.GET, constants.BASE_URL, TestUserStatusNotLoggedIn.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(check_login_status_not_logged_in.get_ret()), "Actual:")
            assert check_login_status_not_logged_in.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_1), "Expected:")
            allure.attach("Err_code: " + str(check_login_status_not_logged_in.get_err_code()), "Actual:")
            assert check_login_status_not_logged_in.get_err_code() == constants.ERR_CODE_1
