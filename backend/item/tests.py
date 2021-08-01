import pytest
from django.urls import reverse
from rest_framework import status
from item.serializers import ItemSerializer
from item.models import Item
from ..conftest import model_field_list


@pytest.mark.usefixtures("item", "api_client_with_auth")
def test_retrieve_auction(api_client_with_auth, item):
    """
    Is it good way to concrete data (with serialize)?
    """
    response = api_client_with_auth.get(reverse('item-detail', kwargs={'pk': item.pk}), format='json')
    item_data = ItemSerializer(instance=item)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == item_data.data


@pytest.mark.usefixtures("api_client_with_auth", "response_struct_key_list", "item")
def test_lot_list(api_client_with_auth, response_struct_key_list, item):
    item_fields = model_field_list(Item)

    response = api_client_with_auth.get(reverse('item-list'), format='json')

    assert response.status_code == status.HTTP_200_OK

    response_keys = list(response.data.keys())

    assert response_keys == response_struct_key_list

    if response.data['count'] > 0:
        response_item_keys = list(response.data['results'][0].keys())
        assert next(item_fields) == response_item_keys


@pytest.mark.usefixtures("api_client_with_auth", "item_data")
def test_post_auction(api_client_with_auth, item_data):
    response = api_client_with_auth.post(reverse('item-list'), data=item_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
