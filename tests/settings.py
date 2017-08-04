from django.conf.global_settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_d_c1ey&hn%ps^^@!bzj9ns#$d7afhi)vvw&t!qty83k-g4tkg'

DEBUG = False
TEMPLATE_DEBUG = DEBUG


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tests',
)

# lean cloud config
# LEANCLOUD_HEADERS = {
#     "X-LC-Id": "<replace your x-lc-id>",
#     "X-LC-Key": "<replace your x-lc-key>",
#     "Content-Type": "application/json"
# }


LEANCLOUD_HEADERS = {
    "X-LC-Id": "K7XwGopwRnNj7QbumCVWzzoP-gzGzoHsz",
    "X-LC-Key": "gRbi4TIFk10Q1vJj2SyKqWT3",
    "Content-Type": "application/json"
}

LEANCLOUD_SMS_NAME = "Epub360"