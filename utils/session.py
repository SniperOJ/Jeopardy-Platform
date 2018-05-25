from functools import wraps


def clear_session(func):
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        request.session.clear()
        return func(request, *args, **kwargs)
    return returned_wrapper
