from data import constants
from data.params import Params


class CheckUserStatus:

    @staticmethod
    def get_test_case(test_case_name):
        check_user_status = {
            "test_check_admin_status_logged_in": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_login_params(constants.ADMIN_USERNAME,
                                                    constants.MD5_PASSWORD, constants.APP_KEY)
            },
            "test_check_user_status_long_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.LONG_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_not_logged_in": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.USER_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_short_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.SHORT_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            }
        }
        return check_user_status[test_case_name]
