import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.logout import Logout


@allure.feature('Logout Request')
class TestLogoutWithShortToken:

    def test_logout_with_short_token(self):
        with allure.step("Send logout request with short token"):
            logout_with_short_token = SendRequest(Logout.get_test_case(
                "test_logout_with_short_token", constants.TMP_TOKEN))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_SHORT_TOKEN, "Expected:")
            allure.attach("Msg: " + logout_with_short_token.get_msg(), "Actual:")
            assert constants.ERR_MSG_SHORT_TOKEN in logout_with_short_token.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(logout_with_short_token.get_ret()), "Actual:")
            assert logout_with_short_token.get_ret() == constants.RET_400