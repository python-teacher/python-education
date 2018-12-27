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


def decorator(f):
    def wrapper(my_name):
        if "Sergiy Budz" != my_name[0] or "Pavlo" != my_name[1]:
            raise ValueError("Permission denied")
        else:
            return f()

    return wrapper


@decorator
def check_perms():
    return "Access is allowed"


def get_user_info(*name):
    return name

print(check_perms(get_user_info("Sergiy Budz","Pavlo")))
