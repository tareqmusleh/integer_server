# -*- coding: utf-8 -*-

import unittest

from ..sequences_generator import baum_sweet_sequence, nth_baum_sweet

class TestBaumSweetSequence(unittest.TestCase):
	"""
	Ensures the methods baum_sweet_sequence and nth_baum_sweet generate the baum_sweet_sequence number properly. Expected output
	came from: https://oeis.org/A086747
	"""

	def test_baum_sweet_sequence_first_15(self):
		""" 
		Ensures that the first 15 terms of the baum_sweet_sequence are generated properly. 
		"""
		first_15 = baum_sweet_sequence(15)
		excepted_output = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]
		self.assertEquals(first_15, excepted_output)


	def test_nth_baum_sweet_0_term(self):
		""" Ensures if 0 is passed in to nth_baum_sweet, then 1 (the first element) is returned. """

		self.assertEquals(nth_baum_sweet(0), 1)


	def test_nth_baum_sweet_1_term(self):
		""" Ensures if 1 is passed in to nth_baum_sweet, then 1 (the second element) is returned. """

		self.assertEquals(nth_baum_sweet(1), 1)


	def test_baum_sweet_sequence_0(self):
		""" Ensures that if 0 is passed into baum_sweet_sequence, an empty list is returned. """

		self.assertEquals(baum_sweet_sequence(0), [])


	def test_baum_sweet_sequence_20th_term(self):
		""" 
		Ensures that the nth_baum_sweet function returns the correct nth element. 
		"""
		self.assertEquals(nth_baum_sweet(20), 0)