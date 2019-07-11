import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.logout import Logout


@allure.feature('Logout Request')
class TestLogoutWithoutUuid:

    def test_log_out_without_uuid(self):
        with allure.step("Send an admin logout request"):
            logout_without_uuid = SendRequest(Logout.get_test_case(
                "test_logout_without_uuid", constants.TMP_TOKEN))

        with allure.step('Checking msg'):
            allure.attach("Msg contains " + constants.ERR_MSG_WITHOUT_UUID, "Expected:")
            allure.attach("Msg: " + logout_without_uuid.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_UUID in logout_without_uuid.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(logout_without_uuid.get_ret()), "Actual:")
            assert logout_without_uuid.get_ret() == constants.RET_400