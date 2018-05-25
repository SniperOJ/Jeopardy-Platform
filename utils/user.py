from django.http import JsonResponse
from django.db.models import Q


def login_required(func):
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        if not check_login(request):
            result = {
                "status": False,
                "result": "You can not do this before loged in! Please login!"
            }
            return JsonResponse(result)
        else:
            return func(request, *args, **kwargs)

    return returned_wrapper


def clear_session(func):
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        request.session.clear()
        return func(request, *args, **kwargs)

    return returned_wrapper


def get_user_id_from_session(request):
    return int(request.session['login'])


from functools import wraps


def check_login(request):
    if 'login' not in request.session:
        return False
    try:
        user_id = int(request.session['login'])
        User.objects.get(id=user_id)
        return True
    except Exception as e:
        print(e)
        return False
