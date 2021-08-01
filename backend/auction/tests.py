import pytest
from django.urls import reverse
from rest_framework import status
from auction.serializers import AuctionSerializer
from auction.models import Auction
from ..conftest import model_field_list


# Is  last import correct????


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


@pytest.mark.usefixtures("api_client_with_auth", "response_struct_key_list", "english_auction")
def test_auction_list(api_client_with_auth, response_struct_key_list, english_auction):
    auction_fields = model_field_list(Auction)  # endless??

    response = api_client_with_auth.get(reverse('auction-list'), format='json')

    assert response.status_code == status.HTTP_200_OK

    response_keys = list(response.data.keys())

    assert response_keys == response_struct_key_list

    if response.data['count'] > 0:
        response_auction_keys = list(response.data['results'][0].keys())
        assert next(auction_fields) == response_auction_keys  # if user for for this generator -> endless generator


@pytest.mark.usefixtures("api_client_with_auth", "english_auction_data", "dutch_auction_data")
def test_post_auction(api_client_with_auth, english_auction_data, dutch_auction_data):
    english_response = api_client_with_auth.post(reverse('auction-list'), data=english_auction_data, format='json')
    dutch_response = api_client_with_auth.post(reverse('auction-list'), data=dutch_auction_data, format='json')

    assert english_response.status_code == status.HTTP_201_CREATED
    assert dutch_response.status_code == status.HTTP_201_CREATED
