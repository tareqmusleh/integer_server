# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View

from .sequences_generator import fibonacci, fibonacci_sequence, nth_happy, happy_sequence, nth_abundant 
from .sequences_generator import abundant_sequence, baum_sweet_sequence, nth_baum_sweet, nth_sphenic, sphenic_sequence
from .mixins import VerifyInputMixin

import json

class NthNumberSequenceView(VerifyInputMixin, View):

	"""
	Returns the nth number in the integer sequence in a JSON response.

	Example response:
	{"nth_term": 0}
	"""

	sequence_to_function = {'fibonacci': fibonacci, 'happy': nth_happy, 'abundant': nth_abundant, 'baumsweet': nth_baum_sweet, 'sphenic': nth_sphenic}

	def get(self, request, *args, **kwargs):
		
		sequence_type = kwargs.get('sequence')
		if not self.is_valid_input(sequence_type):
			return HttpResponseBadRequest("HTTP 400 Bad Request")

		nth_term = kwargs.get('n')
		sequence_function = self.sequence_to_function.get(sequence_type)
		data = {'nth_term': sequence_function(int(nth_term))}
		return HttpResponse(json.dumps(data), content_type='application/json')


class FirstNNumbersView(VerifyInputMixin, View):

	"""
	Returns the first n terms in the integer sequence in a JSON response.

	Example response:
	{"first_terms": [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190]}
	"""

	sequence_to_function = {'fibonacci': fibonacci_sequence, 'happy': happy_sequence, 'abundant': abundant_sequence, 'baumsweet': baum_sweet_sequence, 'sphenic': sphenic_sequence}

	def get(self, request, *args, **kwargs):

		sequence_type = kwargs.get('sequence')
		if not self.is_valid_input(sequence_type):
			return HttpResponseBadRequest("HTTP 400 Bad Request")

		nth_term = kwargs.get('n')
		sequence_function = self.sequence_to_function.get(sequence_type)
		data = {'first_terms': sequence_function(int(nth_term))}
		return HttpResponse(json.dumps(data), content_type='application/json')