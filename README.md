# Django Leancloud SMS
[![Build Status](https://travis-ci.org/edison7500/django-leancloud-sms.svg?branch=master)](https://travis-ci.org/edison7500/django-leancloud-sms)

## 安装
```bash
pip install django-leancloud-sms

# or 

pip install requests # requests be must >= 2.1
git clone https://github.com/edison7500/django-leancloud-sms.git
cd django-leancloud-sms
python setup.py install
 
```

## 使用方法
1. 在 django settings.py 设置以下配置
```python

LEANCLOUD_HEADERS = {
    "X-LC-Id": "<replace your x-lc-id>",
    "X-LC-Key": "<replace your x-lc-key>",
    "Content-Type": "application/json"
}

LEANCLOUD_SMS_NAME = "<replace your name>"

```
2. 在 Django View 中使用
```python
'''
DJANGO Views.py
'''
from django.http import JsonResponse
from leancloud.sms import LeanCloudSMS


def send_sms_view(request):
    phone_num = request.GET.get('num')
    sms = LeanCloudSMS()
    data, msg = sms.send_sms(phone_number=phone_num) # 发送验证码
    return JsonResponse(status=200, data={
                                        'status':data,
                                        'msg':msg
                                    })

def verify_phone_code(request):
    phone_num = request.GET.get('num')
    v_code = request.GET.get('vcode')
    sms = LeanCloudSMS()
    data, msg = sms.verify_phone_code(phone_number=phone_num, verify_code=v_code) # 验证手机验证码
    return JsonResponse(status=200, data={
                                        'status':data,
                                        'msg':msg
                                    })
```