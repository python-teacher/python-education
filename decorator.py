"""
This task contains a few parts:
Write a custom function which returns your name or username.
Write a decorator which allows access for your user and prints 
“Permission denied” for other users.

Tips:
Create get_user_info function which returns your name or username.
Create decorator which raises Exception if get_user_info returns not 
your name or username
Create check_perms function decorated by decorator. This function
returns Allowed access if user validation is successful.
"""


def get_user_info():
    return 'sergiy'


def decorator(allowed_users):
    def wrapper(f):
        if get_user_info() not in allowed_users:
            raise ValueError("Permission denied")
        else:
            return f()

    return wrapper


@decorator(["sergiy", "pavlo"])
def check_perms():
    return "Access is allowed"


print(check_perms)
