from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


def check_user(user):
    return not user.is_authenticated

user_logout_required = user_passes_test(check_user, '/accounts/logout', 'login')

def auth_user_should_not_access(viewfunc):
    return user_logout_required(viewfunc)