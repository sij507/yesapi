from data import constants
from data.params import Params
from common import common


class Register:

    # Register test cases
    @staticmethod
    def get_test_case(test_case_name):
        new_username = common.random_string(10)
        register = {
            "test_register_new_user_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(new_username, constants.MD5_PASSWORD, constants.APP_KEY)},
            "test_register_with_existing_username": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(constants.REGULAR_USERNAME, constants.MD5_PASSWORD,
                                                       constants.APP_KEY)},
            "test_register_with_long_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(new_username, constants.LONG_MD5_PASSWORD, constants.APP_KEY)},
            "test_register_with_short_password": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_register_params(new_username, constants.SHORT_MD5_PASSWORD, constants.APP_KEY)}
        }
        return register[test_case_name]
