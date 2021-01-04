from django.test import TestCase
from django.conf import settings
from django import setup

# Create your tests here.
class TestIndex(TestCase):
    @classmethod
    def setUpTestData(cls):
        if not settings.configured:
            settings.configure(DEBUG=True)
            setup()
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)