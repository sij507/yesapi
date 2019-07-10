import allure
from request.send_request import SendRequest
from data import constants
from data.test_cases.register import Register


@allure.feature('Login Request')
class TestRegisterWithWrongAppKey:

    def test_register_with_wrong_app_key(self):
        with allure.step('Send register request with wrong app key'):
            register_with_wrong_app_key = SendRequest(Register.get_test_case("test_register_with_wrong_app_key"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_406), "Expected:")
            allure.attach("Ret: " + str(register_with_wrong_app_key.get_ret()), "Actual:")
            assert register_with_wrong_app_key.get_ret() == constants.RET_406

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_REGISTER_WRONG_APP_KEY, "Expected:")
            allure.attach("Msg: " + register_with_wrong_app_key.get_msg(), "Actual:")
            assert register_with_wrong_app_key.get_msg() == constants.ERR_MSG_REGISTER_WRONG_APP_KEY
