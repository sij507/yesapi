import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.register import Register


@allure.feature('Login Request')
class TestRegisterWithoutPassword:

    def test_register_without_password(self):
        with allure.step('Send register request without password'):
            register_without_password = SendRequest(Register.get_test_case("test_register_without_password"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_without_password.get_ret()), "Actual:")
            assert register_without_password.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_REGISTER_WITHOUT_PASSWORD, "Expected:")
            allure.attach("Msg: " + register_without_password.get_msg(), "Actual:")
            assert register_without_password.get_msg() == constants.ERR_MSG_REGISTER_WITHOUT_PASSWORD