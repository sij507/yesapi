from data import constants
from data.params import Params


class Logout:

    @staticmethod
    def get_test_case(test_case_name, token):
        logout = {
            "test_logout_with_admin_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, token, constants.APP_KEY)
            },
            "test_logout_with_long_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.LONG_UUID, token, constants.APP_KEY)
            },
            "test_logout_with_short_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.SHORT_UUID, token, constants.APP_KEY)
            },
            "test_logout_without_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    None, token, constants.APP_KEY)
            },
            "test_logout_with_long_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, constants.LONG_TOKEN, constants.APP_KEY)
            },
            "test_logout_with_short_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, constants.SHORT_TOKEN, constants.APP_KEY)
            },
            "test_logout_without_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, None, constants.APP_KEY)
            },
            "test_logout_with_long_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, token, constants.LONG_APP_KEY)
            },
            "test_logout_with_short_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, token, constants.SHORT_APP_KEY)
            },
            "test_logout_with_wrong_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, token, constants.WRONG_APP_KEY)
            },
            "test_logout_without_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(
                    constants.ADMIN_UUID, token, None)
            },
        }
        return logout[test_case_name]