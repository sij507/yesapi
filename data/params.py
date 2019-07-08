
class Params:

    @staticmethod
    def setup_alter_password_params(username, old_password, new_password, app_key):
        params = {
            'service': "App.User.AlterPassword",
            'username': username,
            'old_password': old_password,
            'new_password': new_password,
            'app_key': app_key
        }
        return params

    @staticmethod
    def setup_login_params(username, new_password, app_key):

        params = {
            'service': "App.User.Login",
            'username': username,
            'password': new_password,
            'app_key': app_key
        }
        return params

    @staticmethod
    def setup_check_params(uuid, token, app_key):
        params = {
            'service': "App.User.Check",
            'uuid': uuid,
            'token': token,
            'app_key': app_key
        }
        return params

    @staticmethod
    def setup_logout_params(uuid, admin_token, app_key):
        params = {
            'service': "App.User.Logout",
            'uuid': uuid,
            'token': admin_token,
            'app_key': app_key
        }
        return params

    @staticmethod
    def setup_users_list_params(page, per_page, role, app_key):
        params = {
            'service': "App.User.GetList",
            'page': page,
            'perpage': per_page,
            'role': role,
            'app_key': app_key
        }
        return params

    @staticmethod
    def setup_register_params(username, password, app_key):
        params = {
            'service': "App.User.Register",
            'username': username,
            'password': password,
            'app_key': app_key
        }
        return params

