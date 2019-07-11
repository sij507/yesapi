import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListGetAdmin:

    def test_users_list_get_admin(self):
        with allure.step("Send a get list request with role admin, page 1 and 10 per page"):
            all_admin_list = SendRequest(UsersList.get_test_case("test_users_list_get_admin"))

        with allure.step('Checking if per page is less or equal to 10'):
            is_per_page_less_or_equal_10 = len(all_admin_list.get_users_list()) <= int(constants.PER_PAGE_10)
            allure.attach("Per page is less or equal to 10: True", "Expected:")
            allure.attach("Per page is less or equal to 10: " + str(is_per_page_less_or_equal_10), "Actual:")
            assert is_per_page_less_or_equal_10 is True

        with allure.step('Checking if all users are admin'):
            is_all_users_admin = all_admin_list.is_all_users_admin()
            allure.attach("All users are admin: True", "Expected:")
            allure.attach("All users are admin: " + str(is_all_users_admin), "Actual:")
            assert is_all_users_admin is True

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(all_admin_list.get_ret()), "Actual:")
            assert all_admin_list.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(all_admin_list.get_err_code()), "Actual:")
            assert all_admin_list.get_err_code() == constants.ERR_CODE_0
