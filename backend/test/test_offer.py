import pytest
from base_test import BaseTest
from helpers.url_base import UrlBase

class TestOffer(BaseTest):

    @pytest.mark.django_db
    def test_offer_list(self, api_client_with_auth, response_struct_key_list, offer_field_list, offer):
        super().test_list(api_client_with_auth, response_struct_key_list, offer_field_list, UrlBase.offer)

        # response = api_client_with_auth.get(reverse('offer-list'), format='json')
        # response_keys = list(response.data.keys())
        # assert response.status_code == status.HTTP_200_OK
        # assert response_keys == response_struct_key_list
        # if response.data['count'] > 0:
        #     response_offer_keys = list(response.data['results'][0].keys())
        #     assert offer_field_list == response_offer_keys

    @pytest.mark.django_db
    def test_post_offer(self, api_client_with_auth, offer_field_list, offer_post_data):
        offer_data_list = [offer_post_data]
        super().test_post(api_client_with_auth, offer_field_list, offer_data_list, UrlBase.offer)

        # response = api_client_with_auth.post(reverse('offer-list'), data=offer_post_data, format='json')
        # assert response.status_code == status.HTTP_201_CREATED
