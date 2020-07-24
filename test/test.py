# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from src.myadd import addition


class MathTest(unittest.TestCase):
	def test_addition(self):
		actual = addition(3,4)
		#expected = 8 # 実行結果と一致
		expected = 7 # 実行結果と一致
		self.assertEqual(actual, expected)
