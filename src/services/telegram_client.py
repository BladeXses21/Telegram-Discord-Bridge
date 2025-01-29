from telethon import TelegramClient
from telethon.tl.types import User, Channel, Chat


class TelegramClientService:
    def __init__(self, api_id, api_hash, session_name: str = 'telegram_session'):
        self.client = TelegramClient(session_name, api_id, api_hash)

    async def connect(self):
        await self.client.start()
        print('Telegram client connected!')


    async def disconnect(self):
        await self.client.disconnect()
        print('Telegram client disconnected!')
