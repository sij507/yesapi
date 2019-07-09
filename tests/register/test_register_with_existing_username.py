import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.register import Register


@allure.feature('Register Request')
class TestRegisterWithExistingUsername:

    def test_register_new_user_success(self):
        with allure.step("Send a register request"):
            register_with_existing_username = SendRequest(
                Register.get_test_case("test_register_with_existing_username"))

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(register_with_existing_username.get_ret()), "Actual:")
            assert register_with_existing_username.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_1), "Expected:")
            allure.attach("Err_code: " + str(register_with_existing_username.get_err_code()), "Actual:")
            assert register_with_existing_username.get_err_code() == constants.ERR_CODE_1

        with allure.step('Checking Err_msg'):
            allure.attach("Err_msg " + constants.ERR_MSG_REGISTER_EXISTING_USERNAME, "Expected:")
            allure.attach("Err_msg: " + register_with_existing_username.get_err_msg(), "Actual:")
            assert register_with_existing_username.get_err_msg() == constants.ERR_MSG_REGISTER_EXISTING_USERNAME