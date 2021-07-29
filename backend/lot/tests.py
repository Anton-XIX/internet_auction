from django.urls import reverse
from .models import CustomUser
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


class LotTest(APITestCase):

    def setUp(self):
        test_user = CustomUser.objects.create_user(email='user@test.', password='testpass', username='TestUser',
                                                   first_name='Tester', last_name='Test')

        self.user_test_token = AccessToken.for_user(test_user)
