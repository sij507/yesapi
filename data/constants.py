# URL
BASE_URL = "http://hn216.api.yesapi.cn"

# Request

GET = 'get'
POST = 'post'

# APP KEY
APP_KEY = "814A1BC1B5DD7102AAB47DEAAB70F7A2"

# USERNAME
ADMIN_USERNAME = "sij507@gmail.com"
REGULAR_USERNAME = "ct1e0nk4ykj"
INVALID_USERNAME = "wrong_user"
BANNED_USERNAME = "aqakldxjvj"

# PASSWORD
MD5_PASSWORD = "25d55ad283aa400af464c76d713c07ad"
WRONG_MD5_PASSWORD = "25d55ad283aa400af464c76d713c07aa"
LONG_MD5_PASSWORD = "25d55ad283aa400af464c76d713c07add"
SHORT_MD5_PASSWORD = "25d55ad283aa400af464c76d713c07a"
NEW_PASSWORD = "5e8667a439c68f5145dd2fcbecf02209"

# TOKEN
TMP_TOKEN = "1A34271C39EABC268A427A6AC21ED1840104413D68A41DB630CE4EC17BDA240B"

# ROLE
ROLE_ADMIN = "admin"
ROLE_USER = "user"
ROLE_ALL = "all"

# UUID
ADMIN_UUID = '3316285B59FE032863B0B6BF0778EA6B'
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

# GET LIST PARAMS
DEFAULT_PAGE = "1"
DEFAULT_PER_PAGE = "20"
PER_PAGE_10 = "10"
PER_PAGE_15 = "15"

# LOGIN ERROR MESSAGE
ERR_MSG_LOGIN_FAILED = "登录失败，账号不存在"
ERR_MSG_LOGIN_WRONG_PASSWORD_OR_USERNAME = "登录失败，密码错误或已被封号"
ERR_MSG_LOGIN_PASSWORD_TOO_LONG = "客户端非法请求：password.len应该小于等于32, 但现在password.len = 33。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Login"
ERR_MSG_LOGIN_PASSWORD_TOO_SHORT = "客户端非法请求：password.len应该大于或等于32, 但现在password.len = 31。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Login"

# ALTER PASSWORD ERROR MESSAGE
ERR_MSG_ALTER_PSW_WRONG_PASSWORD_OR_USERNAME = "密码修改失败，原密码错误或账号不存在"
ERR_MSG_ALTER_PSW_PASSWORD_TOO_LONG = "客户端非法请求：old_password.len应该小于等于32, 但现在old_password.len = 33。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.AlterPassword"
ERR_MSG_ALTER_PSW_PASSWORD_TOO_SHORT = "客户端非法请求：old_password.len应该大于或等于32, 但现在old_password.len = 31。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.AlterPassword"
ERR_MSG_ALTER_PSW_PASSWORD_SAME_PASSWORD = "密码修改失败，不能与原来密码相同"

# REGISTER ERROR MESSAGE
ERR_MSG_REGISTER_EXISTING_USERNAME = "用户已注册，不能重复注册"
ERR_MSG_REGISTER_LONG_PASSWORD = "客户端非法请求：password.len应该小于等于32, 但现在password.len = 33。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Register"
ERR_MSG_REGISTER_SHORT_PASSWORD = "客户端非法请求：password.len应该大于或等于32, 但现在password.len = 31。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Register"

# CHECK ERROR MESSAGE
ERR_MSG_CHECK_SHORT_UUID = "客户端非法请求：uuid.len应该大于或等于32, 但现在uuid.len = 31。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Check"
ERR_MSG_CHECK_LONG_UUID = "客户端非法请求：uuid.len应该小于等于32, 但现在uuid.len = 33。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Check"


# LOGOUT ERROR MESSAGE
ERR_MSG_LOGOUT_SHORT_UUID = "客户端非法请求：uuid.len应该大于或等于32, 但现在uuid.len = 31。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Logout"
ERR_MSG_LOGOUT_LONG_UUID = "客户端非法请求：uuid.len应该小于等于32, 但现在uuid.len = 33。噢！你似乎遇到了问题，别担心，请看接口文档：http://hn216.api.yesapi.cn/docs.php?&detail=1&s=App.User.Logout"