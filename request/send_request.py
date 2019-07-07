import requests


class SendRequest:

    def __init__(self, request_method, url, params):
        if request_method == "get":
            self.response = requests.get(url=url, params=params).json()
        if request_method == "post":
            self.response = requests.post(url=url, params=params).json()

    def get_response(self):
        return self.response

    def get_ret(self):
        return self.response['ret']

    def get_err_code(self):
        return self.response['data']['err_code']

    def get_err_msg(self):
        return self.response['data']['err_msg']

    def get_msg(self):
        return self.response['msg']

    def get_total(self):
        return self.response['data']['total']

    def get_uuid(self):
        return self.response['data']['uuid']

    def get_role(self):
        return self.response['data']['role']

    def get_token(self):
        return self.response['data']['token']

    def get_users_list(self):
        return self.response['data']['users']

    def is_all_users_admin(self):
        for user in self.response['data']['users']:
            if user['role'] != "admin":
                print(user['role'])
                return False
        return True

    def is_admin_user_in_the_list(self):
        for user in self.response['data']['users']:
            if user['role'] != "admin":
                return True
        return False

    def is_all_users_type_in_the_list(self):
        is_regular_user_in_the_list = False
        for user in self.response['data']['users']:
            if user['role'] == "user":
                is_regular_user_in_the_list = True

        is_admin_in_the_list = False
        for user in self.response['data']['users']:
            if user['role'] != "admin":
                is_admin_in_the_list = True
        all_user_in_the_list = is_regular_user_in_the_list and is_admin_in_the_list
        return all_user_in_the_list

    def is_user_in_the_list(self, uuid):
        for user in self.response['data']['users']:
            if user['uuid'] == uuid:
                return True
        return False