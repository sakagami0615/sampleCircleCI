# -*- coding: utf-8 -*-

import unittest
from src.myadd import addition

class MathTest(unittest.TestCase):
	def test_addition(self):
		actual = addition(3,4)
		expected = 8 # 実行結果と一致
		self.assertEqual(actual, expected)