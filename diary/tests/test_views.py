from django.test import TestCase, Client
from diary.models import Person, Phone
from diary.views import view_contact

class ViewTest(TestCase):
    def setUp(self):
        self.client_stub = Client()
        self.person = Person(first_name = 'Test',last_name = 'lastTest')
        self.person.save()
        self.phone = Phone(person = self.person,number = '9998889991')
        self.phone.save()

    def test_view_contacts_route(self):
        response = self.client_stub.get('/view/')

        self.assertEquals(response.status_code, 200)

    def test_view_single_contact_route(self):
        response = self.client_stub.get('/view/Test')

        self.assertEqual(response.status_code, 200)

    def test_view_single_contact_contents(self):
        response = self.client_stub.get('/view/Test')

        self.assertTrue(response.content.__contains__(self.person.first_name))

    def tearDown(self):
        self.phone.delete()
        self.person.delete()