from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.user_data = {'email': 'test@example.com', 'username': 'testuser', 'password': 'testpassword'}

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')
        self.user_data = {'email': 'test@example.com', 'username': 'testuser', 'password': 'testpassword'}
        self.client.post(self.register_url, self.user_data, format='json')
    
    def test_user_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')
        self.task_list_url = reverse('task-list')
        self.task_data = {'title': 'Test Task', 'description': 'This is a test task.', 'due_date': '2024-02-20', 'status': 'In Progress'}
        self.user_data = {'email': 'test@example.com', 'username': 'testuser', 'password': 'testpassword'}
        self.user = User.objects.create_user(email=self.user_data['email'], username=self.user_data['username'], password=self.user_data['password'])
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_task_list_authenticated(self):
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_task_authenticated(self):
        response = self.client.post(self.task_list_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    


