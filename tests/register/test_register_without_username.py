import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.register import Register


@allure.feature('Login Request')
class TestRegisterWithoutUsername:

    def test_register_without_username(self):
        with allure.step('Send register request without username'):
            register_without_username = SendRequest(Register.get_test_case("test_register_without_username"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_USERNAME, "Expected:")
            allure.attach("Msg: " + register_without_username.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_USERNAME in register_without_username.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_without_username.get_ret()), "Actual:")
            assert register_without_username.get_ret() == constants.RET_400