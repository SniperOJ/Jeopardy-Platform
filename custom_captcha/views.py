from django.http import JsonResponse
from django.http import HttpResponse
from geetest import GeetestLib
from .settings import GEETEST_ID
from .settings import GEETEST_KEY


def generate_captcha(request):
    user_id = 'test'
    gt = GeetestLib(GEETEST_ID, GEETEST_KEY)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


def validate_captcha(request):
    if request.method == "POST":
        gt = GeetestLib(GEETEST_ID, GEETEST_KEY)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return JsonResponse(result)
    return HttpResponse("error")
