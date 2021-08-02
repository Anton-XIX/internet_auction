import pytest
from datetime import datetime, timedelta
from user.models import CustomUser
from lot.models import Lot
from auction.models import Auction
from auction.variables import AuctionType
from item.models import Item
from offer.variables import OfferType
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient


from django.db import connections
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# #
# def run_sql(sql):
#     conn = psycopg2.connect(database='test_auction_dev', user='auction',password='auction_pass', host='db', port='5432')
#     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.close()
# #
# #
# @pytest.fixture(scope='session')
# def django_db_setup(django_db_use_migrations):
#     from django.conf import settings
#     settings.DATABASES['default']['NAME'] = 'test_auction_dev'
#
#     # run_sql('DROP DATABASE IF EXISTS test_auction_dev')
#     # run_sql('CREATE DATABASE test_auction_dev TEMPLATE auction_dev ')
#     print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#     yield
#     for connection in connections.all():
#         connection.close()
#     # run_sql('DROP DATABASE test_auction_dev')
# # ENGINE": "django.db.backends.postgresql",
# #         "NAME": "auction_dev",
# #         "USER": os.environ.get("SQL_USER", "auction"),
# #         "PASSWORD": os.environ.get("SQL_PASSWORD", "auction_pass"),
# #         "HOST": os.environ.get("SQL_HOST", "localhost"),
# #         "PORT": os.environ.get("SQL_PORT", "5432"),
#
# #
# @pytest.mark.django_db
# @pytest.fixture(scope="function")
# def user_tt(django_db_blocker):
#     with django_db_blocker.unblock():
#         return CustomUser.objects.create_user(email='user@test.by', password='testpass', username='TestUser',
#                                           first_name='Tester', last_name='Test')

@pytest.fixture
def user(db) -> CustomUser:

    """
    Does 'yield' better than 'return' in my case?

    If scope set as 'session' -> unable to get this fixture from user/test.py
    """
    user = CustomUser.objects.create_user(email='user@test.by', password='testpass', username='TestUser',
                                          first_name='Tester', last_name='Test')



    yield user



@pytest.fixture
def english_auction(db) -> Auction:
    auction = Auction.objects.create(type=AuctionType.English, start_price=20.00, reserve_price=20.00,
                                     end_date=datetime.now() + timedelta(hours=2), current_price=25.00,
                                     buy_now_price=150.00)

    yield auction
    auction.delete()


@pytest.fixture
def item(db) -> Item:
    item = Item.objects.create(title='Test item', description='Test descr')

    yield item
    item.delete()


@pytest.fixture
def lot(db, english_auction, item, user) -> Lot:
    lot = Lot.objects.create(item=item, auction=english_auction, user=user)
    yield lot
    lot.delete()


@pytest.fixture
def response_struct_key_list() -> list:
    keys = ['count', 'total_pages', 'size', 'results']
    yield keys


@pytest.fixture
def item_field_list() -> list:
    fields = [
        "id",
        "title",
        "description",
        "photo"
    ]
    yield fields


@pytest.fixture
def english_auction_post_data() -> dict:
    data = {
        "type": "En",
        "start_price": 12,
        "reserve_price": 50,
        "end_date": datetime.now() + timedelta(hours=2),
        "current_price": 25,
        "buy_now_price": 50,
        "is_buy_now_available": True,
        "deactivate": True
    }
    yield data


@pytest.fixture
def dutch_auction_post_data() -> dict:
    data = {
        "type": "Nl",
        "start_price": 12,
        "reserve_price": 50,
        "end_date": datetime.now() + timedelta(hours=2),
        "current_price": 25,
        "update_frequency": 10,
        "bid_step": 1,
        "buy_now_price": 50,
        "is_buy_now_available": True,
        "deactivate": True
    }
    yield data


@pytest.fixture
def item_post_data() -> dict:
    data = {
        "title": "Test title",
        "description": "Test descr",
        "photo": None,
    }
    yield data


@pytest.fixture
def offer_post_data(english_auction, user) -> dict:
    data = {
        "auction": english_auction.pk,
        "offer_price": english_auction.current_price + 10,
        "offer_type": OfferType.Bid
    }
    yield data


@pytest.fixture
def auction_field_list() -> list:
    fields = [
        "id",
        "type",
        "start_price",
        "reserve_price",
        "end_date",
        "current_price",
        "update_frequency",
        "bid_step", "buy_now_price",
        "is_buy_now_available",
        "deactivate"
    ]
    yield fields


@pytest.fixture
def lot_field_list(lot) -> list:
    fields = [
        "id",
        "title",
        "description",
        "photo",
        "auction_id",
        "type",
        "start_price",
        "reserve_price",
        "end_date",
        "current_price",
        "update_frequency",
        "bid_step",
        "buy_now_price",
        "deactivate",
        "is_buy_now_available"
    ]
    yield fields


@pytest.fixture
def api_client_with_auth(user):
    # user = CustomUser.objects.create_user(email='user@test.by', password='testpass', username='TestUser',
    #                                       first_name='Tester', last_name='Test')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client
