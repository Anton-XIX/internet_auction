import pytest
from django.urls import reverse
from rest_framework import status
from lot.serializers import LotNestedSerializer


# @pytest.mark.usefixtures("lot", "api_client_with_auth")
# def test_retrieve_lot(api_client_with_auth, lot):
#
#     response = api_client_with_auth.get(reverse('lot-detail', kwargs={'pk': lot.pk}), format='json')
#     lot_data = LotNestedSerializer(instance=lot)
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data == lot_data.data


# @pytest.mark.usefixtures("api_client_with_auth", "response_struct_key_list")
# def test_lot_list(api_client_with_auth, response_struct_key_list):

#     item_fields = model_field_list(Item)
#     auction_fields = model_field_list(Auction)
#     lot_fields = model_field_list(Lot)
#
#     response = api_client_with_auth.get(reverse('lot-list'), format='json')
#
#     response_lot_keys = response.data.keys()
#     response_auction_keys = response.data.keys()
#
#     assert response.data.keys() == response_struct_key_list
#
#     assert response.status_code == status.HTTP_200_OK
#     # assert response.data == lot_data.data
