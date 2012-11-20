from django.test import TestCase, Client

class ViewTest(TestCase):
    def setUp(self):
        self.client_stub = Client()

    def test_view_contacts_route(self):
        response = self.client_stub.get('/view/')

        self.assertEquals(response.status_code, 200)
