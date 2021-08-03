import pytest
from django.urls import reverse
from rest_framework import status
from item.serializers import ItemSerializer


class TestItem:

    @pytest.mark.django_db
    def test_retrieve_item(self, api_client_with_auth, item):

        response = api_client_with_auth.get(reverse('item-detail', kwargs={'pk': item.pk}), format='json')
        item_data = ItemSerializer(instance=item)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == item_data.data

    @pytest.mark.django_db
    def test_lot_list(self, api_client_with_auth, response_struct_key_list, item_field_list, item):
        response = api_client_with_auth.get(reverse('item-list'), format='json')

        assert response.status_code == status.HTTP_200_OK

        response_keys = list(response.data.keys())

        assert response_keys == response_struct_key_list

        if response.data['count'] > 0:
            response_item_keys = list(response.data['results'][0].keys())
            assert item_field_list == response_item_keys

    @pytest.mark.django_db
    def test_post_item(self, api_client_with_auth, item_post_data):
        response = api_client_with_auth.post(reverse('item-list'), data=item_post_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED