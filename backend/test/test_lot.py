import pytest
from base_test import BaseTest
from helpers.url_base import UrlBase


class TestLot(BaseTest):
    @pytest.mark.django_db
    def test_retrieve_lot(self, api_client_with_auth, lot_field_list, lot):
        super().test_retrieve(api_client_with_auth, lot_field_list, lot, UrlBase.lot)

        # response = api_client_with_auth.get(reverse('lot-detail', kwargs={'pk': lot.pk}), format='json')
        # assert response.status_code == status.HTTP_200_OK
        # response_keys = list(response.data.keys())
        # assert response_keys == lot_field_list

    @pytest.mark.django_db
    def test_lot_list(self, api_client_with_auth, response_struct_key_list, lot_field_list):
        super().test_list(api_client_with_auth, response_struct_key_list, lot_field_list, UrlBase.lot)

        # response = api_client_with_auth.get(reverse('lot-list'), format='json')
        # response_keys = list(response.data.keys())
        # assert response.status_code == status.HTTP_200_OK
        # assert response_keys == response_struct_key_list
        # response_lot_keys = response.data['results'][0].keys()
        # if response.data['count'] > 0:
        #     response_lot_keys = list(response.data['results'][0].keys())
        #     assert lot_field_list == response_lot_keys

    @pytest.mark.django_db
    def test_post_lot(self, api_client_with_auth, lot_post_data, lot_field_list):
        lot_data_list = [lot_post_data]
        super().test_post(api_client_with_auth, lot_field_list, lot_data_list, UrlBase.lot)

        # response = api_client_with_auth.post(reverse('lot-list'), data=lot_post_data, format='json')
        # assert response.status_code == status.HTTP_201_CREATED
        # response_lot_keys = list(response.data.keys())
        # assert response_lot_keys == lot_field_list
