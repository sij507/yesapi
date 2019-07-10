from data import constants
from data.params import Params
from common import common


class Register:

    @staticmethod
    def get_test_case(test_case_name):
        new_username = common.random_string(10)
        register = {
            "test_register_new_user_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, new_username, constants.MD5_PASSWORD)
            },
            "test_register_with_existing_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, constants.REGULAR_USERNAME, constants.MD5_PASSWORD)
            },
            "test_register_with_short_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, constants.SHORT_USERNAME, constants.MD5_PASSWORD)
            },
            "test_register_with_long_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, constants.LONG_USERNAME, constants.MD5_PASSWORD)
            },
            "test_register_without_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, None, constants.MD5_PASSWORD)
            },
            "test_register_with_long_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, new_username, constants.LONG_MD5_PASSWORD)
            },
            "test_register_with_short_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, new_username, constants.SHORT_MD5_PASSWORD)
            },
            "test_register_without_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.APP_KEY, new_username, None)
            },
            "test_register_with_short_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.SHORT_APP_KEY, new_username, constants.MD5_PASSWORD)
            },
            "test_register_with_long_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.LONG_APP_KEY, new_username, constants.MD5_PASSWORD)
            },
            "test_register_with_wrong_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    constants.WRONG_APP_KEY, new_username, constants.MD5_PASSWORD)
            },
            "test_register_without_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(
                    None, new_username, constants.MD5_PASSWORD)
            }
        }
        return register[test_case_name]
