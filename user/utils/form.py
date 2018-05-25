from django.http import JsonResponse
from functools import wraps


def not_existed_keys(key_list, data_list):
    result = []
    for key in key_list:
        if key not in data_list:
            result.append(key)
    return result


def check_params(params):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(request, *args, **wkargs):
            invalid_keys = not_existed_keys(params, request.POST)
            if len(invalid_keys) != 0:
                result = {
                    "status": False,
                    "reason": "Please input the following fields: %s" % (",".join(invalid_keys))
                }
                return JsonResponse(result)
            else:
                return func(request, *args, **wkargs)
        return return_wrapper
    return func_wrapper
