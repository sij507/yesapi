from data import constants
from data.params import Params


class Logout:

    @staticmethod
    def get_test_case(test_case_name, token):
        logout = {
            "test_logout_with_admin_success": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(constants.ADMIN_UUID, token,
                                                     constants.APP_KEY)
            },
            "test_logout_with_long_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(constants.LONG_UUID, token,
                                                     constants.APP_KEY)
            },
            "test_logout_with_short_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_logout_params(constants.SHORT_UUID, token,
                                                     constants.APP_KEY)}
        }
        return logout[test_case_name]