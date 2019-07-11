import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListGetAll:

    def test_users_list_get_all(self):
        with allure.step("Send a get list request with role all, page 1 and default 30 per page"):
            all_users_list = SendRequest(UsersList.get_test_case("test_users_list_get_all"))

        with allure.step('Checking if per page is less or equal 30'):
            is_per_page_30 = len(all_users_list.get_users_list()) <= int(constants.PER_PAGE_30)
            allure.attach("Per page is 330: True", "Expected:")
            allure.attach("Per page is " + str(is_per_page_30), "Actual:")
            assert is_per_page_30 is True

        with allure.step('Checking if all user type return'):
            is_all_users_return = all_users_list.is_all_users_type_in_the_list()
            allure.attach("All users type return: True", "Expected:")
            allure.attach("All users type return: " + str(is_all_users_return), "Actual:")
            assert is_all_users_return is True

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(all_users_list.get_ret()), "Actual:")
            assert all_users_list.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(all_users_list.get_err_code()), "Actual:")
            assert all_users_list.get_err_code() == constants.ERR_CODE_0