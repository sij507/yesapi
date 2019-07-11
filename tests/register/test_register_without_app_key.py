import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.register import Register


@allure.feature('Login Request')
class TestRegisterWithoutAppKey:

    def test_register_without_app_key(self):
        with allure.step('Send register request without app key'):
            register_without_app_key = SendRequest(Register.get_test_case("test_register_without_app_key"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + constants.ERR_MSG_WITHOUT_APP_KEY, "Expected:")
            allure.attach("Msg: " + register_without_app_key.get_msg(), "Actual:")
            assert constants.ERR_MSG_WITHOUT_APP_KEY in register_without_app_key.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_without_app_key.get_ret()), "Actual:")
            assert register_without_app_key.get_ret() == constants.RET_400