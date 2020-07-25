from src.saturation import saturation
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class MathTest(unittest.TestCase):

    def test_saturation(self):
        test_datas = [
            {'value': 1, 'high': 10, 'low': 5, 'expect': 5},
            {'value': 7, 'high': 10, 'low': 5, 'expect': 7},
            {'value': 15, 'high': 10, 'low': 5, 'expect': 10}
        ]
        for data in test_datas:
            actual = saturation(data['value'], data['high'], data['low'])
            self.assertEqual(actual, data['expect'])
