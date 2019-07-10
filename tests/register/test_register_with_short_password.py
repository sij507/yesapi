import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.register import Register


@allure.feature('Register Request')
class TestRegisterShortPassword:

    def test_register_with_short_password(self):
        with allure.step("Send a register request with short password"):
            register_with_short_password = SendRequest(
                Register.get_test_case("test_register_with_short_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_with_short_password.get_ret()), "Actual:")
            assert register_with_short_password.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_REGISTER_SHORT_PASSWORD, "Expected:")
            allure.attach("Msg: " + register_with_short_password.get_msg(), "Actual:")
            assert register_with_short_password.get_msg() == constants.ERR_MSG_REGISTER_SHORT_PASSWORD
