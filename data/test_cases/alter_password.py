from data import constants
from data.params import Params


class AlterPassword:

    @staticmethod
    def get_test_case(test_case_name):
        alter_password = {
            "test_alter_password_success": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_long_old_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.LONG_MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_short_old_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.SHORT_MD5_PASSWORD,
                    constants.MD5_PASSWORD)
            },
            "test_alter_password_with_wrong_old_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.WRONG_MD5_PASSWORD,
                    constants.MD5_PASSWORD)
            },
            "test_alter_password_without_old_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, None, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_long_new_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.LONG_MD5_PASSWORD)
            },
            "test_alter_password_with_short_new_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD,
                    constants.SHORT_MD5_PASSWORD)
            },
            "test_alter_password_without_new_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, None)
            },
            "test_alter_password_with_same_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.MD5_PASSWORD)
            },
            "test_alter_password_reset_back_password": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.NEW_PASSWORD, constants.MD5_PASSWORD)
            },
            "test_alter_password_with_nonexistent_username": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.NONEXISTENT_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_short_username": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.SHORT_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_long_username": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, constants.LONG_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_without_username": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.APP_KEY, None, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_wrong_app_key": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.WRONG_APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_short_app_key": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.SHORT_APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_with_long_app_key": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    constants.LONG_APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            },
            "test_alter_password_without_app_key": {
                "method": constants.POST,
                "url": constants.BASE_URL,
                "params": Params.setup_alter_password_params(
                    None, constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.NEW_PASSWORD)
            }
        }

        return alter_password[test_case_name]