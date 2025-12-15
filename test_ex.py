import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from app import app
#import app as tested_app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        #tested_app.app.config['TESTING'] = True
        self.app =app.test_client()
        self.app.testing = True

    def test_success_add(self):
        r = self.app.get('/calc?a=1&b=4&op=add')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')

    def test_success_sub(self):
        r = self.app.get('/calc?a=9&b=4&op=sub')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')

    def test_success_mul(self):
        r = self.app.get('/calc?a=1&b=5&op=mul')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')

    def test_success_div(self):
        r = self.app.get('/calc?a=5&b=1&op=div')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')


if __name__=='__main__':
    unittest.main()

