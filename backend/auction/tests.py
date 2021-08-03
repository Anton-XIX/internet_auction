import pytest
from django.urls import reverse
from rest_framework import status
from auction.serializers import AuctionSerializer

#

# def test_kek(user_tt):
#
#     assert 1
#
# @pytest.mark.django_db(transaction=True)
# @pytest.mark.usefixtures("english_auction", "api_client_with_auth")
# def test_retrieve_auction(api_client_with_auth, english_auction):
#     response = api_client_with_auth.get(reverse('auction-detail', kwargs={'pk': english_auction.id}), format='json')
#     # response_data = AuctionSerializer(data=response.data)
#     # response_data.is_valid()
#     auction_data = AuctionSerializer(instance=english_auction)
#
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data == auction_data.data
#
# @pytest.mark.django_db(transaction=True)
# @pytest.mark.usefixtures("api_client_with_auth", "response_struct_key_list", "english_auction")
# def test_auction_list(api_client_with_auth, response_struct_key_list, auction_field_list, english_auction):
#     response = api_client_with_auth.get(reverse('auction-list'), format='json')
#
#     assert response.status_code == status.HTTP_200_OK
#
#     response_keys = list(response.data.keys())
#
#     assert response_keys == response_struct_key_list
#
#     if response.data['count'] > 0:
#         response_auction_keys = list(response.data['results'][0].keys())
#         assert auction_field_list == response_auction_keys  # if use 'for' for   auction_fields generator -> endless generator
#
# @pytest.mark.django_db(transaction=True)
# @pytest.mark.usefixtures("api_client_with_auth", "english_auction_post_data", "dutch_auction_post_data")
# def test_post_auction(api_client_with_auth, english_auction_post_data, dutch_auction_post_data):
#     english_response = api_client_with_auth.post(reverse('auction-list'), data=english_auction_post_data, format='json')
#     dutch_response = api_client_with_auth.post(reverse('auction-list'), data=dutch_auction_post_data, format='json')
#     breakpoint()
#     assert english_response.status_code == status.HTTP_201_CREATED
#     assert dutch_response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db(transaction=True)
# @pytest.mark.usefixtures("api_client_with_auth", "response_struct_key_list", "english_auction","english_auction_post_data", "dutch_auction_post_data")

class TestU:

    def test_retrieve_auction(self,api_client_with_auth, english_auction):
        response = api_client_with_auth.get(reverse('auction-detail', kwargs={'pk': english_auction.id}), format='json')
        # response_data = AuctionSerializer(data=response.data)
        # response_data.is_valid()
        auction_data = AuctionSerializer(instance=english_auction)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == auction_data.data


    def test_auction_list(self,api_client_with_auth, response_struct_key_list, auction_field_list, english_auction):
        response = api_client_with_auth.get(reverse('auction-list'), format='json')

        assert response.status_code == status.HTTP_200_OK

        response_keys = list(response.data.keys())

        assert response_keys == response_struct_key_list

        if response.data['count'] > 0:
            response_auction_keys = list(response.data['results'][0].keys())
            assert auction_field_list == response_auction_keys  # if use 'for' for   auction_fields generator -> endless generator


    def test_post_auction(self,api_client_with_auth, english_auction_post_data, dutch_auction_post_data):
        english_response = api_client_with_auth.post(reverse('auction-list'), data=english_auction_post_data,
                                                     format='json')
        dutch_response = api_client_with_auth.post(reverse('auction-list'), data=dutch_auction_post_data, format='json')
        breakpoint()
        assert english_response.status_code == status.HTTP_201_CREATED
        assert dutch_response.status_code == status.HTTP_201_CREATED