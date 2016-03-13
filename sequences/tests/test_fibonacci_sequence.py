# -*- coding: utf-8 -*-

import unittest

from ..sequences_generator import fibonacci, fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):
	"""
	Ensures the methods fibonacci and fibonacci_sequence generate the fibonacci_sequence properly. Expected output
	came from: https://oeis.org/A000045
	"""

	def test_fibonacci_sequence_first_15(self):
		""" 
		Ensures that the first 15 terms of the fibonacci_sequence are generated properly. 
		"""

		first_15 = fibonacci_sequence(15)
		excepted_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
		self.assertEquals(first_15, excepted_output)


	def test_fibonacci_sequence_first_term(self):

		first_term = fibonacci(0)
		excepted_output = 0
		self.assertEquals(first_term, excepted_output)

	def test_fibonacci_sequence_20th_term(self):
		""" 
		Ensures that the fibonacci function returns the correct nth element. 
		"""

		term_20 = fibonacci(20)
		excepted_output = 6765
		self.assertEquals(term_20, excepted_output)




