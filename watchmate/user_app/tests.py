from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your tests here.



 
class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'test',
            'password2': 'test',
        }
        
        response = self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example',password='test')
        
    def test_login(self):
        response = self.client.post(reverse('login'),{
            'username': 'example',
            'password': 'test',
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        



