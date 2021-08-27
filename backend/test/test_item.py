import pytest
from base_test import BaseTest
from helpers.url_base import UrlBase


class TestItem(BaseTest):

    @pytest.mark.django_db
    def test_retrieve_item(self, api_client_with_auth, item_field_list, item):
        super().test_retrieve(api_client_with_auth, item_field_list, item, UrlBase.item)

        # response = api_client_with_auth.get(reverse('item-detail', kwargs={'pk': item.pk}), format='json')
        # assert response.status_code == status.HTTP_200_OK
        # response_item_keys = list(response.data.keys())
        # assert response_item_keys == item_field_list

    @pytest.mark.django_db
    def test_lot_list(self, api_client_with_auth, response_struct_key_list, item_field_list, item):
        super().test_list(api_client_with_auth, response_struct_key_list, item_field_list, UrlBase.item)

        # response = api_client_with_auth.get(reverse('item-list'), format='json')
        # assert response.status_code == status.HTTP_200_OK
        # response_keys = list(response.data.keys())
        # assert response_keys == response_struct_key_list
        # if response.data['count'] > 0:
        #     response_item_keys = list(response.data['results'][0].keys())
        #     assert item_field_list == response_item_keys

    @pytest.mark.django_db
    def test_post_item(self, api_client_with_auth, item_field_list, item_post_data):
        item_data_list = [item_post_data]

        super().test_post(api_client_with_auth, item_field_list, item_data_list, 'item')

        # response = api_client_with_auth.post(reverse('item-list'), data=item_post_data, format='json')
        # assert response.status_code == status.HTTP_201_CREATED
        # response_item_keys = list(response.data.keys())
        # assert response_item_keys == item_field_list
