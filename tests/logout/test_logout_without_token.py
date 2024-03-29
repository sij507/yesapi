import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.logout import Logout


@allure.feature('Login Request')
class TestLogoutWithoutToken:

    def test_logout_without_token(self):
        with allure.step('Send logout request without token'):
            log_out_without_token = SendRequest(
                Logout.get_test_case("test_logout_without_token",  constants.TMP_TOKEN))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_TOKEN, "Expected:")
            allure.attach("Msg: " + log_out_without_token.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_TOKEN in log_out_without_token.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(log_out_without_token.get_ret()), "Actual:")
            assert log_out_without_token.get_ret() == constants.RET_400
