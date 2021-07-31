import pytest
from django.urls import reverse
from rest_framework import status
from lot.serializers import LotNestedSerializer


@pytest.mark.usefixtures("lot", "api_client_with_auth")
def test_retrieve_lot(api_client_with_auth, lot):
    """
    Is it good way to concrete data (with serialize)?
    """
    response = api_client_with_auth.get(reverse('lot-detail', kwargs={'pk': lot.pk}), format='json')
    lot_data = LotNestedSerializer(instance=lot)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == lot_data.data
