import pytest
from django.urls import reverse
from rest_framework import status

#
# @pytest.mark.usefixtures("api_client_with_auth", "offer_post_data")
# def test_post_offer(api_client_with_auth, offer_post_data):
#     response = api_client_with_auth.post(reverse('offer-list'), data=offer_post_data, format='json')
#
#     assert response.status_code == status.HTTP_201_CREATED
