import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Check User Status Request')
class TestCheckUserStatusLongUuid:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up check user login params'):
            TestCheckUserStatusLongUuid.params = Params.setup_check_params(
                constants.LONG_UUID, constants.TMP_TOKEN, constants.APP_KEY)

    def test_user_status_not_logged_in(self):
        with allure.step("Send an user login request(not logged in"):
            check_login_status_with_long_uuid = SendRequest(
                constants.GET, constants.BASE_URL,TestCheckUserStatusLongUuid.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(check_login_status_with_long_uuid.get_ret()), "Actual:")
            assert check_login_status_with_long_uuid.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_CHECK_LONG_UUID, "Expected")
            allure.attach("Msg: " + check_login_status_with_long_uuid.get_msg(), "Actual:")
            assert check_login_status_with_long_uuid.get_msg() == constants.ERR_MSG_CHECK_LONG_UUID
