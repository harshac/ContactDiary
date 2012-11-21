from django.template.loader import render_to_string
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

    def test_add_contact_route(self):
        response = self.client_stub.get('/add/')

        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response,'add.html')

    def test_create_contact_successful_route(self):
        response = self.client_stub.post('/create',data = {'first_name' : 'test', 'last_name':'test', 'email':'blah@blah.com', 'address':'jklj', 'city':'fds', 'state':'fd', 'country':'fds', 'pincode':'4444', 'number':'9999900000'})

        self.assertEqual(response.status_code, 302)

    def test_create_contact_unsuccessful_route(self):
        response = self.client_stub.post('/create',data = {'first_name' : 'test_name', 'last_name':'test', 'email':'blah@blah.com', 'address':'jklj', 'city':'fds', 'state':'fd', 'country':'fds', 'pincode':'4444', 'number':'9999900000'})

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.phone.delete()
        self.person.delete()