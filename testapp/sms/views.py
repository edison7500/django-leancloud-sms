# coding=utf-8

from django.http import JsonResponse
from django.views.generic import View

from leancloud.sms import LeanCloudSMS
from leancloud.exceptions import LeanCloudException, PhoneNumberException


class SMSCodeView(View):
    http_method_names = ['post_ajax', 'post']
    sender_class = LeanCloudSMS

    def get_sms_class(self, **kwargs):
        return self.sender_class(**kwargs)

    def process_send_sms(self, requests):
        phone_num = requests.POST.get('num', None)
        assert phone_num is not None, Exception(u"手机号不能为空")
        self.sms = self.get_sms_class()
        try:
            status, msg = self.sms.send_sms(phone_number=phone_num)
            res = {
                'msg': msg,
            }
            return JsonResponse(data=res, status=200)
        except PhoneNumberException as e:
            res = {'msg': e.message}
            return JsonResponse(data=res, status=400)
        except LeanCloudException as e:
            res = {'msg': e.message}
            return JsonResponse(data=res, status=400)

    def post(self, request, *args, **kwargs):
        return self.process_send_sms(request)