from data import constants
from data.params import Params


class CheckUserStatus:

    @staticmethod
    def get_test_case(test_case_name, token=None):
        check_user_status = {
            "test_check_admin_status_logged_in": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, token, constants.APP_KEY)
            },
            "test_check_user_status_not_logged_in": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.USER_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_with_wrong_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.WRONG_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_with_short_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.SHORT_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_with_long_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.LONG_UUID, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_without_uuid": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    None, constants.TMP_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_with_wrong_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.WRONG_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_with_short_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.SHORT_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_with_long_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.LONG_TOKEN, constants.APP_KEY)
            },
            "test_check_user_status_without_token": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, None, constants.APP_KEY)
            },
            "test_check_user_status_with_wrong_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.TMP_TOKEN, constants.WRONG_APP_KEY)
            },
            "test_check_user_status_with_short_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.TMP_TOKEN, constants.SHORT_APP_KEY)
            },
            "test_check_user_status_with_long_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.TMP_TOKEN, constants.LONG_APP_KEY)
            },
            "test_check_user_status_without_app_key": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_check_params(
                    constants.ADMIN_UUID, constants.TMP_TOKEN, None)
            },
        }
        return check_user_status[test_case_name]