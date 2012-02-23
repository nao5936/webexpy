import unittest2
from nose.plugins.attrib import attr
from webex.error import WebExError
from webex.base_controller import BaseController
from webex.event_controller import EventController
import helper
import logger

# these integration tests are normally commented out so we don't incur their hits on every run of our test suite
class BaseControllerTest(unittest2.TestCase):

    def setUp(self):
        print "\n"
        self.account = helper.get_account()

    @attr('api')
    def test_bad_account(self):
        self.account.webex_id = 'bad_webex_id'
        self.account.password = 'bad_password'
        with self.assertRaises(WebExError):
            self.account.rebuild_request_xml_template()
            EventController(self.account).list_()

    def test_invalid_site_name(self):
        self.account.site_name = 'invalid_si@#$%^te_name'
        with self.assertRaises(WebExError):
            self.account.rebuild_request_xml_template()
            EventController(self.account).list_()

    @attr('api')
    def test_wrong_site_name(self):
        self.account.site_name = 'bad_site_name'
        with self.assertRaises(WebExError):
            self.account.rebuild_request_xml_template()
            EventController(self.account).list_()

    @attr('api')
    def test_version(self):
        version = BaseController(self.account).get_api_version()
        self.assertIn('WebEx XML API V', version)

    @attr('api')
    def test_major_version(self):
        self.assertEquals(5, BaseController(self.account).major_version)

    @attr('api')
    def test_password(self):
        self.assertTrue(BaseController(self.account).password_required)

if __name__ == '__main__':
    unittest2.main()


