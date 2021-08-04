from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from auction.models import Auction


class BaseTest:

    @classmethod
    def test_retrieve(cls, api_client: APIClient, model_field_list: list, model_instance, url_basename: str):

        response = api_client.get(reverse(f'{url_basename}-detail', kwargs={'pk': model_instance.id}),
                                  format='json')

        assert response.status_code == status.HTTP_200_OK

        response_keys = list(response.data.keys())

        assert response_keys == model_field_list

    @classmethod
    def test_list(cls, api_client, response_struct_key_list, model_field_list, url_basename):
        response = api_client.get(reverse(f'{url_basename}-list'), format='json')

        assert response.status_code == status.HTTP_200_OK

        response_keys = list(response.data.keys())

        assert response_keys == response_struct_key_list

        if response.data['count'] > 0:
            response_nested_keys = list(response.data['results'][0].keys())
            assert model_field_list == response_nested_keys

    @classmethod
    def test_post(cls, api_client, model_field_list, post_data, url_basename):

        for data in post_data:
            response = api_client.post(reverse(f'{url_basename}-list'), data=data,
                                       format='json')
            assert response.status_code == status.HTTP_201_CREATED
            response_keys = list(response.data.keys())  # [*dict]
            assert model_field_list == response_keys
