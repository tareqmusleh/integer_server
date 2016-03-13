import json

from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from ..views import NthNumberSequenceView, FirstNNumbersView


class NthNumberSequenceViewTests(TestCase):

	"""
	Ensures the NthNumberSequenceView is functioning properly.
	""" 

	def setUp(self):
	
		self.factory = RequestFactory()

	def test_bad_request(self):
		"""
		Ensures a 400 bad request is returned when the sequence requested is not supported.
		"""

		url = reverse('nth_term', kwargs={'sequence': 'unsupported', 'n': '5'})
		request = self.factory.get(url)
		self.view = NthNumberSequenceView(request=request)
		response = self.view.get(request)
		self.assertEquals(response.status_code, 400)


	def test_200_request(self):
		"""
		Ensures a 200 status code and json with the correct value for the nth term in the
		sequence is returned.
		"""
		params = {'sequence': 'fibonacci', 'n': '5'}
		url = reverse('nth_term', kwargs=params)
		request = self.factory.get(url)
		excepted_json_response = json.dumps({'nth_term': 5})
		self.view = NthNumberSequenceView(request=request)
		response = self.view.get(request, **params)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(response.content, excepted_json_response)


class FirstNNumbersViewViewTests(TestCase):

	"""
	Ensures the FirstNNumbersView is functioning properly.
	""" 

	def setUp(self):
	
		self.factory = RequestFactory()

	def test_bad_request(self):
		"""
		Ensures a 400 bad request is returned when the sequence requested is not supported.
		"""

		url = reverse('n_terms', kwargs={'sequence': 'unsupported', 'n': '5'})
		request = self.factory.get(url)
		self.view = FirstNNumbersView(request=request)
		response = self.view.get(request)
		self.assertEquals(response.status_code, 400)


	def test_200_request(self):
		"""
		Ensures a 200 status code and json with the correct value for the first n terms
		is returned in the json response.
		"""
		params = {'sequence': 'fibonacci', 'n': '5'}
		url = reverse('n_terms', kwargs=params)
		request = self.factory.get(url)
		excepted_json_response = json.dumps({'first_terms': [0, 1, 1, 2, 3]})
		self.view = FirstNNumbersView(request=request)
		response = self.view.get(request, **params)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(response.content, excepted_json_response)