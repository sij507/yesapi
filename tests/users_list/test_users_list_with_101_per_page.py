import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListWith101PerPage:

    def test_users_list_with_101_per_page(self):
        with allure.step("Send a get list request with 101 per page"):
            users_list_with_101_per_page = SendRequest(UsersList.get_test_case("test_users_list_with_101_per_page"))

        with allure.step('Checking msg'):
            allure.attach("Msg: " + str(constants.ERR_MSG_USERS_LIST_101_PER_PAGE), "Expected:")
            allure.attach("Msg: " + str(users_list_with_101_per_page.get_msg()), "Actual:")
            assert constants.ERR_MSG_USERS_LIST_101_PER_PAGE in users_list_with_101_per_page.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(users_list_with_101_per_page.get_ret()), "Actual:")
            assert users_list_with_101_per_page.get_ret() == constants.RET_400