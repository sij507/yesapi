import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.logout import Logout


@allure.feature('Logout Request')
class TestLogoutWithLongUuid:

    def test_logout_with_long_uuid(self):
        with allure.step("Send logout request with long uuid"):
            logout_with_long_uuid = SendRequest(
                Logout.get_test_case("test_logout_with_long_uuid", constants.TMP_TOKEN))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_LONG_UUID, "Expected:")
            allure.attach("Msg: " + logout_with_long_uuid.get_msg(), "Actual:")
            assert constants.ERR_MSG_LONG_UUID in logout_with_long_uuid.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(logout_with_long_uuid.get_ret()), "Actual:")
            assert logout_with_long_uuid.get_ret() == constants.RET_400