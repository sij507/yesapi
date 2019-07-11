import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListWith0PerPage:

    def test_users_list_with_0_per_page(self):
        with allure.step("Send a get list request with 0 per page"):
            users_list_with_0_per_page = SendRequest(UsersList.get_test_case("test_users_list_with_0_per_page"))

        with allure.step('Checking if per page is equal to 0'):
            is_per_page_equal_to_0 = len(users_list_with_0_per_page.get_users_list()) == int(constants.PER_PAGE_0)
            allure.attach("Per page is equal to 0: True", "Expected:")
            allure.attach("Per page is equal to 0" + str(is_per_page_equal_to_0), "Actual:")
            assert is_per_page_equal_to_0 is True

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(users_list_with_0_per_page.get_ret()), "Actual:")
            assert users_list_with_0_per_page.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(users_list_with_0_per_page.get_err_code()), "Actual:")
            assert users_list_with_0_per_page.get_err_code() == constants.ERR_CODE_0