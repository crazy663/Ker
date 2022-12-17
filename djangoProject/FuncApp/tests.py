from django.test import TestCase, Client



class ContTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index_page_GET_is_working(self):
        response = self.client.get(path='')
        self.assertEqual(response.status_code, 200)

    def test_index_page_POST_is_working(self):
        response = self.client.post(path='', data={'InValue': '"@sndk"'})
        self.assertEqual(response.status_code, 200)

    def test_index_page_returned_headers(self):
        response = self.client.post(path='', data={'InValue': '"@sndk"'})
        self.assertEqual(response.headers.get('Content-Type'), 'text/html; charset=utf-8')
