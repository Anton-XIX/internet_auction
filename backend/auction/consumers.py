import json

from channels.generic.websocket import AsyncWebsocketConsumer


class AuctionConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['pk']
        self.auction_group_name = f'auction_current_price_{self.auction_id}'
        await self.channel_layer.group_add(
            self.auction_group_name, self.channel_name
        )
        self.groups.append(self.auction_group_name)
        await self.accept()

    async def message(self, event):
        await self.send(text_data=json.dumps({"bid": event["message"]}))

#
# import json
#
# from channels.generic.websocket import AsyncWebsocketConsumer
#
#
# class AuctionConsumer(AsyncWebsocketConsumer):
#
#     async def connect(self):
#         await self.channel_layer.group_add(
#             "auction_current_price", self.channel_name
#         )
#         self.groups.append("auction_current_price")
#         await self.accept()
#
#     async def message(self, event):
#         await self.send(text_data=json.dumps({"bid": event["message"]}))
