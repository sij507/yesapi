import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.register import Register


@allure.feature('Register Request')
class TestRegisterShortAppKey:

    def test_register_with_short_app_key(self):
        with allure.step("Send a register request with short app key"):
            register_with_short_app_key = SendRequest(
                Register.get_test_case("test_register_with_short_app_key"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_SHORT_APP_KEY, "Expected:")
            allure.attach("Msg: " + register_with_short_app_key.get_msg(), "Actual:")
            assert constants.ERR_MSG_SHORT_APP_KEY in register_with_short_app_key.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_with_short_app_key.get_ret()), "Actual:")
            assert register_with_short_app_key.get_ret() == constants.RET_400