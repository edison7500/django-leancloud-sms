# coding=utf-8
import re
import requests
import json
import logging

from django.conf import settings
from .exceptions import LeanCloudException, PhoneNumberException

logger = logging.getLogger(__name__)

headers = getattr(settings, 'LEANCLOUD_HEADERS')


class LeanCloudSMS(object):
    cell_phone_match = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    url = 'https://leancloud.cn/1.1/requestSmsCode'
    # verify_url = 'https://leancloud.cn/1.1/verifySmsCode/%s?mobilePhoneNumber=%s' % (verify_code, phone_number)
    verify_url = 'https://leancloud.cn/1.1/verifySmsCode/'

    def __init__(self, name=None):
        if name is None:
            self.name = getattr(settings, 'LEANCLOUD_SMS_NAME', None)
        else:
            self.name = name
        self.headers = getattr(settings, 'LEANCLOUD_HEADERS', None)

        assert self.name is not None
        assert self.headers is not None

    def _check_phone_num(self, phone_number):
        if self.cell_phone_match.match(phone_number):
            return True
        else:
            return False

    def send_sms(self, phone_number):
        if not self._check_phone_num(phone_number):
            raise PhoneNumberException(u'请输入正确的手机号')

        payload = {'mobilePhoneNumber': str(phone_number)}
        payload.update({
            'name': self.name,
        })
        res = requests.post(self.url, json=payload, headers=headers)
        if res.status_code == 200:
            # data = res.json()
            return True, 'success'
        else:
            msg = res.json()['error']
            raise LeanCloudException(u"{msg}".format(msg=msg))

    def verify_phone_code(self, phone_number, verify_code):
        if not self._check_phone_num(phone_number):
            raise PhoneNumberException(u'请输入正确的手机号')
        _verify_url = "{url}{code}?mobilePhoneNumber={phone_num}".format(
            url=self.verify_url,
            code=verify_code,
            phone_num=phone_number,
        )
        res = requests.post(_verify_url, headers=headers)
        if res.status_code == 200:
            return True, 'success'
        else:
            msg = res.json()['error']
            raise LeanCloudException(u"{msg}".format(msg=msg))

