import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.logout import Logout


@allure.feature('Logout Request')
class TestLogoutWithLongToken:

    def test_log_out_with_long_token(self):
        with allure.step("Send logout request with long token"):
            logout_with_long_token = SendRequest(
                Logout.get_test_case("test_logout_with_long_token", constants.TMP_TOKEN))

        with allure.step('Checking msg'):
            allure.attach("Msg contains:" + constants.ERR_MSG_LONG_TOKEN, "Expected:")
            allure.attach("Msg: " + logout_with_long_token.get_msg(), "Actual:")
            assert constants.ERR_MSG_LONG_TOKEN in logout_with_long_token.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(logout_with_long_token.get_ret()), "Actual:")
            assert logout_with_long_token.get_ret() == constants.RET_400