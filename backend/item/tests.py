import pytest
from django.urls import reverse
from rest_framework import status
from item.serializers import ItemSerializer


@pytest.mark.usefixtures("item", "api_client_with_auth")
def test_retrieve_auction(api_client_with_auth, item):
    """
    Is it good way to concrete data (with serialize)?
    """
    response = api_client_with_auth.get(reverse('item-detail', kwargs={'pk': item.pk}), format='json')
    item_data = ItemSerializer(instance=item)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == item_data.data
