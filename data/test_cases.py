from common import constants
from common.params import Params


class LoginTestCases:

    def __init__(self):
    login = {
        "test_login_with_admin_success": {
            "method": constants.GET,
            "url": constants.BASE_URL,
            "data": Params.setup_login_params(
                        constants.ADMIN_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)},
        "test_login_with_regular_user_success": {
            "method": constants.GET,
            "url": constants.BASE_URL,
            "data": Params.setup_login_params(
                constants.REGULAR_USERNAME, constants.MD5_PASSWORD, constants.APP_KEY)},
    }
