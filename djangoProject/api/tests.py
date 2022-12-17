from django.urls import reverse
from rest_framework.test import APITestCase


class ParsingTests(APITestCase):

    def test_pars_correct(self):
        url = 'http://127.0.0.1:8000/api/@sndk'
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "urlpath": "@sndk",
            "result": "['ЕГОР', '[сундучный архив]', 'сыс тв']"
        })
