from data import constants
from data.params import Params


class AlterPassword:

    @staticmethod
    def get_test_case(test_case_name):
        alter_password = {
            "test_alter_password_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD,
                    constants.APP_KEY)
            },
            "test_alter_password_with_long_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.REGULAR_USERNAME, constants.LONG_MD5_PASSWORD, constants.NEW_PASSWORD,
                    constants.APP_KEY)
            },
            "test_alter_password_with_same_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.REGULAR_USERNAME, constants.MD5_PASSWORD,
                    constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_alter_password_with_short_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.REGULAR_USERNAME, constants.SHORT_MD5_PASSWORD,
                    constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_alter_password_with_wrong_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.REGULAR_USERNAME, constants.WRONG_MD5_PASSWORD,
                    constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_alter_password_with_invalid_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.INVALID_USERNAME, constants.MD5_PASSWORD,
                    constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_alter_password_reset_back_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.REGULAR_USERNAME, constants.NEW_PASSWORD,
                    constants.MD5_PASSWORD, constants.APP_KEY)
            }
        }
        return alter_password[test_case_name]