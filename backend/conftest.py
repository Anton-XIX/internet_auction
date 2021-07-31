import pytest
from datetime import datetime, timedelta

from django.urls import reverse
from user.models import CustomUser
from lot.models import Lot
from auction.models import Auction
from auction.variables import AuctionType
from item.models import Item
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.test import APIClient


@pytest.fixture
def user(db) -> CustomUser:
    """
    Does 'yield' better than 'return' in my case?

    If scope set as 'session' -> unable to get this fixture from user/test.py
    """
    user = CustomUser.objects.create_user(email='user@test.by', password='testpass', username='TestUser',
                                          first_name='Tester', last_name='Test')
    yield user
    user.delete()


@pytest.fixture
def english_auction(db) -> Auction:
    auction = Auction.objects.create(type=AuctionType.English, start_price=20.00, reserve_price=20.00,
                                     end_date=datetime.now() + timedelta(hours=2), current_price=25.00, buy_now_price=150.00)

    yield auction
    auction.delete()


@pytest.fixture
def item(db) -> Item:
    item = Item.objects.create(title='Test item', description='Test descr')

    yield item
    item.delete()

@pytest.fixture
def lot(db,english_auction,item,user) -> Lot:
    lot = Lot.objects.create(item=item, auction=english_auction, user=user)
    yield lot
    lot.delete()


@pytest.fixture
def api_client_with_auth(db,user):
    # user = CustomUser.objects.create_user(email='user@test.by', password='testpass', username='TestUser',
    #                                       first_name='Tester', last_name='Test')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client



