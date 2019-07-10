from data import constants
from data.params import Params


class UsersList:

    @staticmethod
    def get_test_case(test_case_name):
        users_list = {
            "test_users_list_with_app_key_only": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(constants.APP_KEY)
            },
            "test_users_list_get_admin": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_10, constants.ROLE_ADMIN)
            },
            "test_users_list_get_all": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.DEFAULT_PER_PAGE, constants.ROLE_ALL)
            },
            "test_users_list_get_regular_users": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_15, constants.ROLE_USER)
            },
            "test_users_list_without_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(None,
                    str(constants.DEFAULT_PAGE), constants.PER_PAGE_15, constants.ROLE_USER)
            }
        }
        return users_list[test_case_name]
