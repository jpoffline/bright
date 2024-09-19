import unittest
from .utils import count_same_tokens


class Test_count_same_tokensr(unittest.TestCase):
    def test_both_empty(self):
        str1 = ""
        str2 = ""
        result = count_same_tokens(str1, str2)
        self.assertEqual(result, 1)

    def test_various(self):
        tests = [
            {"str1": "", "str2": "", "expected": 1},
            {"str1": "hello1", "str2": "hello2", "expected": 0},
            {"str1": "hello1", "str2": "hello1", "expected": 1},
            {"str1": "hello1 and", "str2": "hello1 and", "expected": 2},
            {"str1": "hello1 and", "str2": "hello1 and1", "expected": 1},
        ]
        for test in tests:
            result = count_same_tokens(test["str1"], test["str2"])
            self.assertEqual(result, test["expected"])
