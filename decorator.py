"""
This task contains a few parts:
Write a custom function which returns your name or username.
Write a allowed_users which allows access for your user and prints 
“Permission denied” for other users.

Tips:
Create get_user_info function which returns your name or username.
Create allowed_users which raises Exception if get_user_info returns not 
your name or username
Create check_perms function decorated by allowed_users. This function
returns Allowed access if user validation is successful.
"""


def get_user_info():
    return 'sergiy'


def allowed_users(users):
    def wrapper(f):
        if get_user_info() not in users:
            raise ValueError("Permission denied")
        else:
            return f()

    return wrapper


@allowed_users(["sergiy", "pavlo"])
def check_perms():
    return "Access is allowed"


print(check_perms)
