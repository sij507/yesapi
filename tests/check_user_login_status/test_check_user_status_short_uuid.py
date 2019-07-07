import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Check User Status Request')
class TestCheckUserStatusShortUuid:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up check user login params'):
            TestCheckUserStatusShortUuid.params = Params.setup_check_params(
                constants.SHORT_UUID, constants.TMP_TOKEN, constants.APP_KEY)

    def test_user_status_not_logged_in(self):
        with allure.step("Send an user login request(not logged in"):
            check_login_status_with_short_uuid = SendRequest(
                constants.GET, constants.BASE_URL,TestCheckUserStatusShortUuid.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(check_login_status_with_short_uuid.get_ret()), "Actual:")
            assert check_login_status_with_short_uuid.get_ret() == constants.RET_400

        with allure.step("Checking msg"):
            allure.attach("Msg: " + constants.ERR_MSG_CHECK_SHORT_UUID, "Expected")
            allure.attach("Msg: " + check_login_status_with_short_uuid.get_msg(), "Actual:")
            assert check_login_status_with_short_uuid.get_msg() == constants.ERR_MSG_CHECK_SHORT_UUID
