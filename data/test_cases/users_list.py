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
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_30, constants.ROLE_ALL)
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
                "params": Params.setup_users_list_params(None)
            },
            "test_users_list_with_long_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(constants.LONG_APP_KEY)
            },
            "test_users_list_with_short_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(constants.SHORT_APP_KEY)
            },
            "test_users_list_with_wrong_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(constants.WRONG_APP_KEY)
            },
            "test_users_list_with_long_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_30, constants.ROLE_USER,
                    constants.LONG_UUID)
            },
            "test_users_list_with_short_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_30, constants.ROLE_USER,
                    constants.SHORT_UUID)
            },
            "test_users_list_with_short_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_30, constants.ROLE_USER,
                    constants.USER_UUID, constants.SHORT_TOKEN)
            },
            "test_users_list_with_long_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_30, constants.ROLE_USER,
                    constants.USER_UUID, constants.LONG_TOKEN)
            },
            "test_users_list_with_101_per_page": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_101)
            },
            "test_users_list_with_0_per_page": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    constants.APP_KEY, str(constants.DEFAULT_PAGE), constants.PER_PAGE_0)
            }
        }
        return users_list[test_case_name]
