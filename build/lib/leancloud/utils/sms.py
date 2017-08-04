# coding=utf-8
__author__ = 'apple'
import requests
import json

# Epub360 应用
# HEADERS = {
#     "X-AVOSCloud-Application-Id": "og3ehvmg9u190wpqt7jvm1wrxo91fsfwsxrkn5pr6qx0vkpj",
#     "X-AVOSCloud-Application-Key": "spaptgnd5ji2zeyceqxj8wi1p39wpurijjzygbr9ym0a9to9",
#     "Content-Type": "application/json"
# }

# 手机验证应用
HEADERS = {
    "X-LC-Id": "K7XwGopwRnNj7QbumCVWzzoP-gzGzoHsz",
    "X-LC-Key": "gRbi4TIFk10Q1vJj2SyKqWT3",
    "Content-Type": "application/json"
}


def send_sms(phonenumber, name='Epub360'):
    flag, msg = verify_number(phonenumber)
    if not flag:
        return flag, msg

    _data = {'mobilePhoneNumber': str(phonenumber)}
    if name:
        _data['name'] = name
    url = 'https://leancloud.cn/1.1/requestSmsCode'
    try:
        r = requests.post(url, json=_data, headers=HEADERS)
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
        r = requests.post(url, headers=HEADERS)
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
