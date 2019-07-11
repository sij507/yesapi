import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.register import Register


@allure.feature('Register Request')
class TestRegisterLongUsername:

    def test_register_with_long_username(self):
        with allure.step("Send a register request with long username"):
            register_with_long_username = SendRequest(
                Register.get_test_case("test_register_with_long_username"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_LONG_USERNAME, "Expected:")
            allure.attach("Msg: " + register_with_long_username.get_msg(), "Actual:")
            assert constants.ERR_MSG_LONG_USERNAME in register_with_long_username.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_with_long_username.get_ret()), "Actual:")
            assert register_with_long_username.get_ret() == constants.RET_400
