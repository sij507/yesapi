import allure
from data import constants
from request.send_request import SendRequest
from data.test_cases.users_list import UsersList


@allure.feature('Get Users List Request')
class TestUsersListWithLongUuid:

    def test_users_list_with_long_uuid(self):
        with allure.step("Send a get list request with long uuid"):
            users_list_with_long_uuid = SendRequest(UsersList.get_test_case("test_users_list_with_long_uuid"))

        with allure.step('Checking msg'):
            allure.attach("Msg contains: " + str(constants.ERR_MSG_LONG_UUID), "Expected:")
            allure.attach("Msg: " + str(users_list_with_long_uuid.get_msg()), "Actual:")
            assert constants.ERR_MSG_LONG_UUID in users_list_with_long_uuid.get_msg()

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_400), "Expected:")
            allure.attach("Ret: " + str(users_list_with_long_uuid.get_ret()), "Actual:")
            assert users_list_with_long_uuid.get_ret() == constants.RET_400