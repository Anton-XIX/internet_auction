from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import pytest




class TestUser:

    @pytest.mark.django_db
    def test_get_token_for_user(self,client, user):
        response = client.post(reverse('token_obtain_pair'), data={'email': user.email, 'password': 'testpass'},
                               format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' and 'refresh' in response.data

    @pytest.mark.django_db
    def test_get_new_token_for_user(self,client, user):
        """
        Need use str(token_instance) because RefreshToken and his parents have no attrib "token".
        Magic method __str__ returns signed token as encoded string.
        Question: How does it works?

        """
        refresh = str(RefreshToken.for_user(user))
        response = client.post(reverse('token_refresh'), data={'refresh': refresh}, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
