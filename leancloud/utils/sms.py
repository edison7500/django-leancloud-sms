# coding=utf-8
__author__ = 'apple'
import requests
import json

from django.conf import settings


headers = getattr(settings, 'LEANCLOUD_HEADERS')


class LeanCloudSMS(object):
    def __init__(self, name):
        self.name = name
        self.headers = getattr(settings, 'LEANCLOUD_HEADERS', None)
        assert self.headers is not  None

    def _check_phone_num(self):
        pass

    def send_sms(self, phone_number):
        pass

    def verify_phone(self, phone_number, verify_code):
        pass


def send_sms(phonenumber, name='Epub360'):
    flag, msg = verify_number(phonenumber)
    if not flag:
        return flag, msg

    _data = {'mobilePhoneNumber': str(phonenumber)}
    if name:
        _data['name'] = name
    url = 'https://leancloud.cn/1.1/requestSmsCode'
    try:
        r = requests.post(url, json=_data, headers=headers)
        result = r.text
        result = json.loads(result)
    except Exception, e:
        return False, e.message
    if result:
        return False, result.get('error', '')
    else:
        return True, 'success'


def verify_phone(phone_number, verify_code):
    try:
        phone_number = int(phone_number)
    except:
        return False, u'请输入正确的手机号'

    if phone_number < 10000000000 or phone_number > 19999999999:
        return False, u'请输入正确的手机号'
    url = 'https://leancloud.cn/1.1/verifySmsCode/%s?mobilePhoneNumber=%s' % (verify_code, phone_number)
    try:
        r = requests.post(url, headers=headers)
        result = r.text
        result = json.loads(result)
    except Exception, e:
        return False, e.message
    if result:
        return False, result.get('error')
    else:
        return True, 'success'


def verify_number(phone_number):
    try:
        phone_number = int(phone_number)
    except:
        return False, u'请输入正确的手机号'

    if phone_number < 10000000000 or phone_number > 19999999999:
        return False, u'请输入正确的手机号'

    return True, ''
