from common import common
from data import constants


class Params:

    @staticmethod
    def setup_alter_password_params(app_key, username, old_password, new_password, uuid=None, token=None):
        tmp_params = {
            'app_key': app_key,
            'new_password': new_password,
            'old_password': old_password,
            'service': "App.User.AlterPassword",
            'username': username,
            'token': token,
            'uuid': uuid
        }
        params = {}
        for key in tmp_params:
            if tmp_params[key] is not None:
                params[key] = tmp_params[key]
        if constants.SIGN:
            params['sign'] = common.generate_sign(params)
        return params

    @staticmethod
    def setup_login_params(username, password, app_key):
        tmp_params = {
            'app_key': app_key,
            'password': password,
            'service': "App.User.Login",
            'username': username,
        }
        params = {}
        for key in tmp_params:
            if tmp_params[key] is not None:
                params[key] = tmp_params[key]
        if constants.SIGN:
            params['sign'] = common.generate_sign(params)
        return params

    @staticmethod
    def setup_check_params(uuid, token, app_key):
        tmp_params = {
            'app_key': app_key,
            'service': "App.User.Check",
            'token': token,
            'uuid': uuid
        }
        params = {}
        for key in tmp_params:
            if tmp_params[key] is not None:
                params[key] = tmp_params[key]
        if constants.SIGN:
            params['sign'] = common.generate_sign(params)
        return params

    @staticmethod
    def setup_logout_params(uuid, token, app_key):
        tmp_params = {
            'app_key': app_key,
            'service': "App.User.Logout",
            'token': token,
            'uuid': uuid
        }
        params = {}
        for key in tmp_params:
            if tmp_params[key] is not None:
                params[key] = tmp_params[key]
        if constants.SIGN:
            params['sign'] = common.generate_sign(params)
        return params

    @staticmethod
    def setup_users_list_params(app_key, page=None, per_page=None, role=None, uuid=None, token=None):
        tmp_params = {
            'app_key': app_key,
            'page': page,
            'perpage': per_page,
            'role': role,
            'service': "App.User.GetList",
            'token': token,
            'uuid': uuid
        }
        params = {}
        for key in tmp_params:
            if tmp_params[key] is not None:
                params[key] = tmp_params[key]
        if constants.SIGN:
            params['sign'] = common.generate_sign(params)
        return params

    @staticmethod
    def setup_register_params(app_key, username, password, uuid=None, token=None, ext_info=None):
        tmp_params = {
            'app_key': app_key,
            'ext_info': ext_info,
            'password': password,
            'service': "App.User.Register",
            'username': username,
            'token': token,
            'uuid': uuid
        }
        params = {}
        for key in tmp_params:
            if tmp_params[key] is not None:
                params[key] = tmp_params[key]
        if constants.SIGN:
            params['sign'] = common.generate_sign(params)
        return params

