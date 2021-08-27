import pytest
from base_test import BaseTest
from helpers.url_base import UrlBase

class TestAuction(BaseTest):

    @pytest.mark.django_db
    def test_retrieve_auction(self, api_client_with_auth, auction_field_list, english_auction):
        super().test_retrieve(api_client_with_auth, auction_field_list, english_auction, UrlBase.auction)

        # response = api_client_with_auth.get(reverse('auction-detail', kwargs={'pk': english_auction.id}), format='json')
        # assert response.status_code == status.HTTP_200_OK
        # response_auction_keys = list(response.data.keys())
        # assert response_auction_keys == auction_field_list

    @pytest.mark.django_db
    def test_auction_list(self, api_client_with_auth, response_struct_key_list, auction_field_list, english_auction):
        super().test_list(api_client_with_auth, response_struct_key_list, auction_field_list, UrlBase.auction)

        # response = api_client_with_auth.get(reverse('auction-list'), format='json')
        # assert response.status_code == status.HTTP_200_OK
        # response_keys = list(response.data.keys())
        # assert response_keys == response_struct_key_list
        # if response.data['count'] > 0:
        #     response_auction_keys = list(response.data['results'][0].keys())
        #     assert auction_field_list == response_auction_keys

    @pytest.mark.django_db
    def test_post_auction(self, api_client_with_auth, english_auction_post_data, dutch_auction_post_data,
                          auction_field_list):
        auction_data_list = [english_auction_post_data, dutch_auction_post_data]

        super().test_post(api_client_with_auth, auction_field_list, auction_data_list,  UrlBase.auction)


        # english_response = api_client_with_auth.post(reverse('auction-list'), data=english_auction_post_data,
        #                                              format='json')
        # dutch_response = api_client_with_auth.post(reverse('auction-list'), data=dutch_auction_post_data, format='json')
        # assert english_response.status_code == status.HTTP_201_CREATED
        # assert dutch_response.status_code == status.HTTP_201_CREATED
        # response_english_auction_keys = list(english_response.data.keys())
        # response_dutch_auction_keys = list(dutch_response.data.keys())
        # assert auction_field_list == response_english_auction_keys
        # assert auction_field_list == response_dutch_auction_keys

# def test_kek(user_tt):
#
#     assert 1
#
