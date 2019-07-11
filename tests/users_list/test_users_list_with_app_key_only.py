import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListWithAppKeyOnly:

    def test_users_list_with_app_key_only(self):
        with allure.step("Send a get list request with app_key_only, default page 1, 20 per page, role all"):
            users_list_with_app_key_only = SendRequest(UsersList.get_test_case("test_users_list_with_app_key_only"))

        with allure.step('Checking if per page is less or equal 20'):
            is_per_page_20 = len(users_list_with_app_key_only.get_users_list()) <= int(constants.DEFAULT_PER_PAGE)
            allure.attach("Per page is 20: True", "Expected:")
            allure.attach("Per page is " + str(is_per_page_20), "Actual:")
            assert is_per_page_20 is True

        with allure.step('Checking if all user type return'):
            is_all_users_return = users_list_with_app_key_only.is_all_users_type_in_the_list()
            allure.attach("All users type return: True", "Expected:")
            allure.attach("All users type return: " + str(is_all_users_return), "Actual:")
            assert is_all_users_return is True

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(users_list_with_app_key_only.get_ret()), "Actual:")
            assert users_list_with_app_key_only.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(users_list_with_app_key_only.get_err_code()), "Actual:")
            assert users_list_with_app_key_only.get_err_code() == constants.ERR_CODE_0