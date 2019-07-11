# URL
BASE_URL = "http://hn216.api.yesapi.cn"

# Request
GET = 'get'
POST = 'post'

APP_KEY = "814A1BC1B5DD7102AAB47DEAAB70F7A2"
WRONG_APP_KEY = "814A1BC1B5DD7102AAB47DEAAB70F7B3"
SHORT_APP_KEY = "814A1BC1B5DD7102AAB47DEAAB70F7A"
LONG_APP_KEY = "814A1BC1B5DD7102AAB47DEAAB70F7A22"


APP_SECRECT = "SqV2BJe3mNCxWBAclU4EE2FsrVhPGENwaPi699L1YEIMR8pEzCzdPZRDRwxBcVoKB9bv0Jivf"


SIGN = True


# USERNAME
ADMIN_USERNAME = "sij507@gmail.com"
REGULAR_USERNAME = "ct1e0nk4ykj"
SHORT_USERNAME = ""
LONG_USERNAME = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"
NONEXISTENT_USERNAME = "nonexistent_username"
BANNED_USERNAME = "aqakldxjvj"


# PASSWORD
MD5_PASSWORD = "25d55ad283aa400af464c76d713c07ad"
WRONG_MD5_PASSWORD = "25d55ad283aa400af464c76d713c07aa"
LONG_MD5_PASSWORD = "25d55ad283aa400af464c76d713c07add"
SHORT_MD5_PASSWORD = "25d55ad283aa400af464c76d713c07a"
NEW_PASSWORD = "5e8667a439c68f5145dd2fcbecf02209"


# TOKEN
TMP_TOKEN = "1A34271C39EABC268A427A6AC21ED1840104413D68A41DB630CE4EC17BDA240B"
WRONG_TOKEN = "1A34271C39EABC268A427A6AC21ED1840104413D68A41DB630CE4ECKKBDA240B"
LONG_TOKEN = "1A34271C39EABC268A427A6AC21ED1840104413D68A41DB630CE4EC17BDA240BA"
SHORT_TOKEN = "1A34271C39EABC268A427A6AC21ED1840104413D68A41DB630CE4EC17BDA240"


# ROLE
ROLE_ADMIN = "admin"
ROLE_USER = "user"
ROLE_ALL = "all"


# UUID
ADMIN_UUID = '3316285B59FE032863B0B6BF0778EA6B'
WRONG_UUID = '3311285B59FE032863B0B6BF07711A11'
USER_UUID = 'B2F8241A00E82CCEAE39B6ECD163A2A2'
BANNED_USER_UUID = 'A4311B03FCE4812644C3506D0B8FEA8B'
SHORT_UUID = 'B2F8241A00E82CCEAE39B6ECD163A2A'
LONG_UUID = 'B2F8241A00E82CCEAE39B6ECD163A2A21'


# ERR CODE
ERR_CODE_0 = 0
ERR_CODE_1 = 1
ERR_CODE_2 = 2


# RET
RET_200 = 200
RET_400 = 400
RET_406 = 406


# GET LIST PARAMS
DEFAULT_PAGE = "1"
DEFAULT_PER_PAGE = "20"
PER_PAGE_10 = "10"
PER_PAGE_15 = "15"
PER_PAGE_30 = "30"
PER_PAGE_101 = "101"
PER_PAGE_0 = "0"

# LOGIN ERROR MESSAGES





# ERROR MESSAGES
ERR_MSG_NONEXISTENT_USERNAME = "登录失败，账号不存在"
ERR_MSG_WRONG_PASSWORD_OR_BANNED_USERNAME = "登录失败，密码错误或已被封号"
ERR_MSG_EXISTING_USERNAME = "用户已注册，不能重复注册"
ERR_MSG_CHECK_WRONG_TOKEN_OR_UUID = "用户未登录，或登录态已过期"
ERR_MSG_WITHOUT_PASSWORD = "客户端非法请求：缺少必要参数password"
ERR_MSG_LONG_PASSWORD = "客户端非法请求：password.len应该小于等于32, 但现在password.len = 33"
ERR_MSG_SHORT_PASSWORD = "客户端非法请求：password.len应该大于或等于32, 但现在password.len = 31"
ERR_MSG_WRONG_PASSWORD_OR_USERNAME = "密码修改失败，原密码错误或账号不存在"
ERR_MSG_OLD_PASSWORD_TOO_LONG = "客户端非法请求：old_password.len应该小于等于32, 但现在old_password.len = 33"
ERR_MSG_OLD_PASSWORD_TOO_SHORT = "客户端非法请求：old_password.len应该大于或等于32, 但现在old_password.len = 31"
ERR_MSG_WITHOUT_OLD_PASSWORD = "客户端非法请求：缺少必要参数old_password"
ERR_MSG_NEW_PASSWORD_TOO_LONG = "客户端非法请求：new_password.len应该小于等于32, 但现在new_password.len = 33"
ERR_MSG_NEW_PASSWORD_TOO_SHORT = "客户端非法请求：new_password.len应该大于或等于32, 但现在new_password.len = 31"
ERR_MSG_WITHOUT_NEW_PASSWORD = "客户端非法请求：缺少必要参数new_password"
ERR_MSG_SAME_PASSWORD = "密码修改失败，不能与原来密码相同"
ERR_MSG_WITHOUT_USERNAME = "客户端非法请求：缺少必要参数username"
ERR_MSG_SHORT_USERNAME = "客户端非法请求：username.len应该大于或等于1, 但现在username.len = 0"
ERR_MSG_LONG_USERNAME = "客户端非法请求：username.len应该小于等于50, 但现在username.len = 51"
ERR_MSG_WITHOUT_APP_KEY = "客户端非法请求：缺少必要参数app_key"
ERR_MSG_WRONG_APP_KEY = "客户端非法请求：非法app_key"
ERR_MSG_SHORT_APP_KEY = "客户端非法请求：app_key.len应该大于或等于32, 但现在app_key.len = 31"
ERR_MSG_LONG_APP_KEY = "客户端非法请求：app_key.len应该小于等于32, 但现在app_key.len = 33"
ERR_MSG_SHORT_UUID = "客户端非法请求：uuid.len应该大于或等于32, 但现在uuid.len = 31"
ERR_MSG_LONG_UUID = "客户端非法请求：uuid.len应该小于等于32, 但现在uuid.len = 33"
ERR_MSG_WITHOUT_UUID = "客户端非法请求：缺少必要参数uuid"
ERR_MSG_WITHOUT_TOKEN = "客户端非法请求：缺少必要参数token"
ERR_MSG_LONG_TOKEN = "客户端非法请求：token.len应该小于等于64, 但现在token.len = 65"
ERR_MSG_SHORT_TOKEN = "客户端非法请求：token.len应该大于或等于64, 但现在token.len = 63"
ERR_MSG_USERS_LIST_101_PER_PAGE = "客户端非法请求：perpage应该小于等于100, 但现在perpage = 101"