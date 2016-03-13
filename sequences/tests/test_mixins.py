# -*- coding: utf-8 -*-

import unittest

from django.core.exceptions import ImproperlyConfigured

from ..mixins import VerifyInputMixin

class TestVerifyInputMixin(unittest.TestCase):
	"""
	Ensures the VerifyInputMixin is functioning properly.
	"""

	def setUp(self):

		self.mixin = VerifyInputMixin()

	def test_valid_sequence_type(self):

		"""
		is_valid_input should return True when the sequence is in sequence_to_function attribute.
		"""

		self.mixin.sequence_to_function = {'fibonacci': 'test'}
		self.assertTrue(self.mixin.is_valid_input('fibonacci'))

	def test_invalid_sequence_type(self):

		"""
		is_valid_input should return False when the sequence is not in 
		sequence_to_function attribute.
		"""

		self.mixin.sequence_to_function = {'fibonacci': 'test'}
		self.assertFalse(self.mixin.is_valid_input('bad'))

	def test_no_sequence_to_function_defined(self):

		"""
		is_valid_input should raise an ImproperlyConfigured exception
		when no sequence_to_function is defined
		"""
		
		self.assertRaises(ImproperlyConfigured, self.mixin.is_valid_input, 'exception')