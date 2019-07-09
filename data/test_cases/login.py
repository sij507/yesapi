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
                    constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)},
            "test_login_with_regular_user_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)},
            "test_login_with_invalid_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.INVALID_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)},
            "test_login_with_long_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.LONG_MD5_PASSWORD, constants.APP_KEY)},
            "test_login_with_short_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.SHORT_MD5_PASSWORD, constants.APP_KEY)},
            "test_login_with_wrong_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(
                    constants.ADMIN_USERNAME, constants.WRONG_MD5_PASSWORD, constants.APP_KEY)},
            "test_login_with_new_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(constants.REGULAR_USERNAME, constants.NEW_PASSWORD,
                                                    constants.APP_KEY)
            }
        }
        return login[test_case_name]
