import allure
from common import constants
import pytest
from request.send_request import SendRequest
from common.params import Params


@allure.feature('Get Users List Request')
class TestUsersListGetRegularUser:
    params = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        with allure.step('Set up regular users list params'):
            TestUsersListGetRegularUser.params = Params.setup_users_list_params(
                str(constants.DEFAULT_PAGE), constants.PER_PAGE_15, constants.ROLE_USER, constants.APP_KEY)

    def test_users_list_get_regular_user(self):
        with allure.step("Send a get list request with role user, page 2 and 15 per page"):
            all_regular_user_list = SendRequest(constants.GET, constants.BASE_URL, TestUsersListGetRegularUser.params)

        with allure.step('Checking Ret'):
            allure.attach("Ret: " + str(constants.RET_200), "Expected:")
            allure.attach("Ret: " + str(all_regular_user_list.get_ret()), "Actual:")
            assert all_regular_user_list.get_ret() == constants.RET_200

        with allure.step('Checking Err_code'):
            allure.attach("Err_code: " + str(constants.ERR_CODE_0), "Expected:")
            allure.attach("Err_code: " + str(all_regular_user_list.get_err_code()), "Actual:")
            assert all_regular_user_list.get_err_code() == constants.ERR_CODE_0

        with allure.step('Checking if per page is less or equal 15'):
            is_per_page_less_or_equal_15 = len(all_regular_user_list.get_users_list()) <= int(constants.PER_PAGE_15)
            allure.attach("Per page is less or equal 15: True", "Expected:")
            allure.attach("Per page is less or equal 15" + str(is_per_page_less_or_equal_15), "Actual:")
            assert is_per_page_less_or_equal_15 is True

        with allure.step('Checking if all user type return'):
            is_all_users_type_return = all_regular_user_list.is_all_users_type_in_the_list()
            allure.attach("All users type return: True", "Expected:")
            allure.attach("All users type return: " + str(all_regular_user_list), "Actual:")
            assert is_all_users_type_return is True
