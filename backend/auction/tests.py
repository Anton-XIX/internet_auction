import pytest
from django.urls import reverse
from rest_framework import status
from auction.serializers import AuctionSerializer


@pytest.mark.usefixtures("english_auction", "api_client_with_auth")
def test_retrieve_auction(api_client_with_auth, english_auction):
    """
    Is it good way to concrete data (with serialize)?
    """
    response = api_client_with_auth.get(reverse('auction-detail', kwargs={'pk': english_auction.id}), format='json')
    # responce_data = AuctionSerializer(data=response.data)
    # responce_data.is_valid()
    auction_data = AuctionSerializer(instance=english_auction)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == auction_data.data
