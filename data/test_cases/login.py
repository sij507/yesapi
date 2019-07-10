from data import constants
from data.params import Params


class Login:

    @staticmethod
    def get_test_case(test_case_name):
        login = {
            "test_login_with_admin_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_regular_user_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_long_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.LONG_MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_short_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.SHORT_MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_wrong_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.WRONG_MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_without_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, None, constants.APP_KEY)
            },
            "test_login_with_new_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.REGULAR_USERNAME, constants.NEW_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_nonexistent_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.NONEXISTENT_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_banned_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.BANNED_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_short_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.SHORT_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_long_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.LONG_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_without_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    None, constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_login_with_wrong_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.WRONG_APP_KEY)
            },
            "test_login_with_short_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.SHORT_APP_KEY)
            },
            "test_login_with_long_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.LONG_APP_KEY)
            },
            "test_login_without_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.MD5_PASSWORD, None)
            }
        }
        return login[test_case_name]
