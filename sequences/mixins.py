# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured

class VerifyInputMixin(object):

	"""
	Validates the sequence_type in the url is supported.
	Requires consuming view to define sequence_to_function which should be
	dictionary containing the mapping of acceptable params to a function.
	Raises ImproperlyConfigured exception if not set.
	"""

	sequence_to_function = None

	def is_valid_input(self, sequence_type):

		""" Validates that the integer sequence in the url is something we support """
		
		if not self.sequence_to_function:
			raise ImproperlyConfigured(
					"%(cls)s is missing sequence_to_function attribute. Define"
                    "%(cls)s.sequence_to_function" % {
                        'cls': self.__class__.__name__
                    }
                )
		return sequence_type and sequence_type in self.sequence_to_function