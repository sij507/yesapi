import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.logout import Logout


@allure.feature('Login Request')
class TestLogoutWithoutAppKey:

    def test_logout_without_app_key(self):
        with allure.step('Send an admin logout request without app key'):
            log_out_without_app_key = SendRequest(
                Logout.get_test_case("test_logout_without_app_key",  constants.TMP_TOKEN))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(log_out_without_app_key.get_ret()), "Actual:")
            assert log_out_without_app_key.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_LOGOUT_WITHOUT_APP_KEY, "Expected:")
            allure.attach("Msg: " + log_out_without_app_key.get_msg(), "Actual:")
            assert log_out_without_app_key.get_msg() == constants.ERR_MSG_LOGOUT_WITHOUT_APP_KEY
