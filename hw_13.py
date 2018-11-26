def input():
        try:
            get_user_info()
            return ('Allowed access')
        except:
            return ('Permission denied')


def get_user_info():
    return 'Sergiy'


print(get_user_info())
print(input())
