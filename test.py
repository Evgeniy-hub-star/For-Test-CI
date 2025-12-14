import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import app as tested_app

class FlaskAppTests(unittest.TestCase):
    def test_success_add(self):
        r = self.app.get('calc?a=9&b=5&op=add')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')

if __name__=='__main__':
    unittest.main()

