from data import constants
from data.params import Params


class UsersList:

    @staticmethod
    def get_test_case(test_case_name):
        users_list = {
            "test_users_list_get_admin": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    str(constants.DEFAULT_PAGE), constants.PER_PAGE_10, constants.ROLE_ADMIN, constants.APP_KEY)
            },
            "test_users_list_get_all": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    str(constants.DEFAULT_PAGE), constants.DEFAULT_PER_PAGE, constants.ROLE_ALL, constants.APP_KEY)
            },
            "test_users_list_get_regular_users": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    str(constants.DEFAULT_PAGE), constants.PER_PAGE_15, constants.ROLE_USER, constants.APP_KEY)
            }
        }
        return users_list[test_case_name]
