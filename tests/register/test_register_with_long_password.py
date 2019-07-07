import allure
from common import constants
from request.send_request import SendRequest
from common.params import Params
from common import common


@allure.feature('Register Request')
class TestRegisterLongPassword:

    def test_register_with_long_password(self):
        with allure.step('Set up new user register params'):
            new_username = common.random_string(10)
            register_params = Params.setup_register_params(new_username, constants.LONG_MD5_PASSWORD, constants.APP_KEY)

        with allure.step("Send a register request"):
            register_with_long_password = SendRequest(constants.GET, constants.BASE_URL, register_params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(register_with_long_password.get_ret()), "Actual:")
            assert register_with_long_password.get_ret() == constants.RET_400

        with allure.step('Checking msg'):
            allure.attach("Msg " + constants.ERR_MSG_REGISTER_LONG_PASSWORD, "Expected:")
            allure.attach("Msg: " + register_with_long_password.get_msg(), "Actual:")
            assert register_with_long_password.get_msg() == constants.ERR_MSG_REGISTER_LONG_PASSWORD
