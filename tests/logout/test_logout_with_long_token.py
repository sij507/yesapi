import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.logout import Logout


@allure.feature('Logout Request')
class TestLogoutWithLongToken:

    def test_log_out_with_long_token(self):
        with allure.step("Send an admin logout request with long token"):
            manager_logout_with_long_token = SendRequest(
                Logout.get_test_case("test_logout_with_long_token", constants.TMP_TOKEN))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(manager_logout_with_long_token.get_ret()), "Actual:")
            assert manager_logout_with_long_token.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGOUT_LONG_TOKEN, "Expected:")
            allure.attach("Msg: " + manager_logout_with_long_token.get_msg(), "Actual:")
            assert manager_logout_with_long_token.get_msg() == constants.ERR_MSG_LOGOUT_LONG_TOKEN