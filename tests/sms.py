from django.test import TestCase
from leancloud.sms import LeanCloudSMS


class LeanCloudSMSTestCase(TestCase):
    def setUp(self):
        self.sms = LeanCloudSMS()

    def test_send_verify_code(self):
        self.sms.send_sms('18618288917')

