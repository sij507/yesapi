from data import constants
from data.params import Params
from common import common


class TestCases:

    @staticmethod
    def get_login_tc(test_case_name):
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

    @staticmethod
    def get_logout_tc(test_case_name, token):
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

    @staticmethod
    def get_alter_password_tc(test_case_name):
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

    # Register test cases
    @staticmethod
    def get_register_tc(test_case_name):
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

    @staticmethod
    def get_users_list_tc(test_case_name):
        users_list = {
            "test_users_list_get_admin": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    str(constants.DEFAULT_PAGE), constants.PER_PAGE_10, constants.ROLE_ADMIN, constants.APP_KEY)
            },
            "test_users_list_get_all": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    str(constants.DEFAULT_PAGE), constants.DEFAULT_PER_PAGE, constants.ROLE_ALL, constants.APP_KEY)
            },
            "test_users_list_get_regular_users": {
                "method": constants.GET,
                "url": constants.BASE_URL,
                "params": Params.setup_users_list_params(
                    str(constants.DEFAULT_PAGE), constants.PER_PAGE_15, constants.ROLE_USER, constants.APP_KEY)
            }
        }
        return users_list[test_case_name]

    @staticmethod
    def get_check_user_status_tc(test_case_name):
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
