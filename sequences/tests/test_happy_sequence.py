# -*- coding: utf-8 -*-

import unittest

from ..sequences_generator import nth_happy, happy_sequence

class TestHappyNumberSequence(unittest.TestCase):
	"""
	Ensures the methods nth_happy and happy_sequence used for generating happy numbers
	are functioning properly. Expected output came from: https://oeis.org/A007770
	"""

	def test_happy_sequence_first_15(self):
		""" 
		Ensures that the first 15 terms of the happy_sequence are generated properly. 
		"""

		first_15 = happy_sequence(15)
		excepted_output = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82]
		self.assertEquals(first_15, excepted_output)


	def test_happy_sequence_1_term(self):
		""" Ensures the nth_happy function returns 2nd element when 1 is passed """

		self.assertEquals(nth_happy(1), 7)

	def test_nth_happy_0(self):
		""" Ensures that if 0 is passed into nth_happy, then the first happy element (0) is returned. """

		self.assertEquals(nth_happy(0), 1)

	def test_happy_sequence_0(self):
		""" Ensures that if 0 is passed into happy_sequence, an empty list is returned. """

		self.assertEquals(happy_sequence(0), [])

	def test_happy_sequence_20th_term(self):
		""" 
		Ensures that the happy_sequence function returns the correct nth element. 
		"""

		term_20 = nth_happy(19)
		excepted_output = 100
		self.assertEquals(term_20, excepted_output)
