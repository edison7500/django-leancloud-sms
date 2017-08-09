from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.


class SMSViewTestCase(TestCase):

    def test_can_send_a_code(self):
        data = {
            'num': '<cell-phone>'
        }
        res = self.client.post('/sms/', data=data)
        self.assertEqual(res.status_code, 400)