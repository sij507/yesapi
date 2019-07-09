import allure
import pytest
from data import constants
from request.send_request import SendRequest
from data.test_cases.register import Register
from data.test_cases.users_list import UsersList


@allure.feature('Register Request')
class TestRegisterNewUserSuccess:

    @pytest.mark.skip(reason="Skip it")
    def test_register_new_user_success(self):
        with allure.step("Send a users list request before register"):
            users_list_before_register = SendRequest(UsersList.get_test_case("test_users_list_get_all"))

        with allure.step("Get number of users before new user registers"):
            num_of_users_before_register = users_list_before_register.get_total()

        with allure.step("Send a register request"):
            success_register = SendRequest(Register.get_test_case("test_register_new_user_success"))

        with allure.step("send a users list request after register"):
            new_username_uuid = success_register.get_uuid()
            users_list_after_register = SendRequest(UsersList.get_test_case("test_users_list_get_all"))

        with allure.step("Get number of users before new user registers"):
            num_of_users_after_register = users_list_after_register.get_total()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(success_register.get_ret()), "Actual:")
            assert success_register.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(success_register.get_err_code()), "Actual:")
            assert success_register.get_err_code() == constants.ERR_CODE_0

        with allure.step('Checking if new user in the list'):
            is_new_user_in_the_list = users_list_after_register.is_user_in_the_list(new_username_uuid)
            allure.attach("Is new user in the list: True", "Expected:")
            allure.attach("Is new user in the list: " + str(is_new_user_in_the_list), "Actual:")
            assert is_new_user_in_the_list is True

        with allure.step("Checking if total users increased by one after register"):
            is_total_users_increased_by_one = num_of_users_before_register + 1 == num_of_users_after_register
            allure.attach("Is new user in the list: True", "Expected:")
            allure.attach("Is new user in the list: " + str(is_total_users_increased_by_one), "Actual:")
            assert is_total_users_increased_by_one
