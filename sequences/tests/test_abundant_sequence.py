# -*- coding: utf-8 -*-

import unittest

from ..sequences_generator import nth_abundant, abundant_sequence

class TestAbundantSequence(unittest.TestCase):
	"""
	Ensures the methods abundant_sequence and nth_abundant generate the abundant number properly. Expected output
	came from: https://oeis.org/A005101
	"""

	def test_abundant_sequence_first_15(self):
		""" 
		Ensures that the first 15 terms of the abundant_sequence are generated properly. 
		"""

		first_15 = abundant_sequence(15)
		excepted_output = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72]
		self.assertEquals(first_15, excepted_output)


	def test_nth_abundant_0_term(self):
		""" Ensures if 0 is passed in to nth_abundant, then the first abundant element (12) is returned """

		self.assertEquals(nth_abundant(0), 12)


	def test_abundant_sequence_zero_term(self):
		""" Ensures that if 0 is passed into abundtant_sequence, an empty list is returned. """

		self.assertEquals(abundant_sequence(0), [])


	def test_abundant_sequence_second_term(self):
		""" Test that if 1 is passed into nth_abundant, then the 2nd term is returned. """

		first_term = nth_abundant(1)
		excepted_output = 18
		self.assertEquals(first_term, excepted_output)


	def test_abundant_sequence_20th_term(self):
		""" 
		Ensures that the nth_abundant function returns the correct nth element. 
		"""

		term_20 = nth_abundant(19)
		excepted_output = 90
		self.assertEquals(term_20, excepted_output)