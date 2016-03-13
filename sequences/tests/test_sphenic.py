# -*- coding: utf-8 -*-

import unittest

from ..sequences_generator import sphenic_sequence, nth_sphenic

class TestSphenicSequence(unittest.TestCase):
	"""
	Ensures the methods sphenic_sequence and nth_sphenic methods function properly. Expected output
	came from: https://oeis.org/A007304
	"""

	def test_sphenic_sequence_first_20(self):
		""" 
		Ensures that the first 15 terms of the sphenic_sequence are generated properly. 
		"""
		first_20 = sphenic_sequence(20)
		excepted_output = [30, 42, 66, 70, 78, 102, 105, 110, 114, 130, 138, 154, 165, 170, 174, 182, 186, 190, 195, 222]
		self.assertEquals(first_20, excepted_output)


	def test_nth_sphenic_0_term(self):
		""" Ensures if 0 is passed in to nth_sphenic, then 30 (the first term) is returned. """

		self.assertEquals(nth_sphenic(0), 30)


	def test_nth_sphenic_1_term(self):
		""" Ensures if 1 is passed in to nth_sphenic, then 42 (the second term) is returned. """

		self.assertEquals(nth_sphenic(1), 42)


	def test_sphenic_sequence_0(self):
		""" Ensures that if 0 is passed into sphenic_sequence, an empty list is returned. """

		self.assertEquals(sphenic_sequence(0), [])


	def test_sphenic_sequence_25th_term(self):
		""" 
		Ensures that the nth_sphenic function returns the correct nth element. 
		"""
		self.assertEquals(nth_sphenic(25), 258)