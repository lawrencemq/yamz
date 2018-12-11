import os
import unittest

from environments import Environment


class EnvironmentTestCase(unittest.TestCase):

    def setUp(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.environment = Environment(base, "settings.yaml")
        self.bad_environment = Environment("/fake/path", "settings.yaml")

    def test_file_not_found(self):
        with self.assertRaises(EnvironmentError) as e:
            self.bad_environment.load("global")
            self.assertEqual(e.msg, "/fake/path/settings.yaml was not found!")

    def test_environment_not_loaded(self):
        with self.assertRaises(EnvironmentError) as e:
            home = self.bad_environment.TEST
            self.assertEqual(e.msg, "Tried to access key `HOME` before "
                                    "environment was loaded!")

    def test_load_environment(self):
        os.environ.setdefault("TEST", "/fake/home")
        self.environment.load("global")
        self.assertEqual(self.environment.TEST, "/fake/home")
