import pytest
from django.urls import reverse
from rest_framework import status
from lot.serializers import LotNestedSerializer


class TestLot:
    @pytest.mark.django_db
    def test_retrieve_lot(self, api_client_with_auth, lot):
        response = api_client_with_auth.get(reverse('lot-detail', kwargs={'pk': lot.pk}), format='json')
        lot_data = LotNestedSerializer(instance=lot)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == lot_data.data

    @pytest.mark.django_db
    def test_lot_list(self, api_client_with_auth, response_struct_key_list,lot_field_list):

        response = api_client_with_auth.get(reverse('lot-list'), format='json')

        response_keys = list(response.data.keys())

        assert response.status_code == status.HTTP_200_OK

        assert response_keys == response_struct_key_list

        response_lot_keys = response.data['results'][0].keys()

        if response.data['count'] > 0:
            response_lot_keys = list(response.data['results'][0].keys())
            assert lot_field_list == response_lot_keys  # if use 'for' for   auction_fields generator -> endless generator
