import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListWithShortToken:

    def test_users_list_with_short_token(self):
        with allure.step("Send a get list request with short token"):
            users_list_with_short_token = SendRequest(UsersList.get_test_case("test_users_list_with_short_token"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + str(constants.ERR_MSG_SHORT_TOKEN), "Expected:")
            allure.attach("Msg: " + str(users_list_with_short_token.get_msg()), "Actual:")
            assert constants.ERR_MSG_SHORT_TOKEN in users_list_with_short_token.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(users_list_with_short_token.get_ret()), "Actual:")
            assert users_list_with_short_token.get_ret() == constants.RET_400