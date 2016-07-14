from common.request import Request
import unittest


class TestRequest(unittest.TestCase):

    def test_some_method(self):
        request = Request()
        self.assertEqual(request.some_method(2, 2), 4)
