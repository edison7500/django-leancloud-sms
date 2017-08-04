# Django Leancloud SMS


## 安装
```bash
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
2. 
```python
from leancloud.sms import LeanCloudSMS

sms = LeanCloudSMS()

sms.send_sms('13000000001') # 发送验证码

sms.verify_phone_code('13000000001', verify_code='xxxx') # 验证手机验证码

```