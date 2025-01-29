import asyncio

from telethon import events
from telethon.tl.types import User, Channel, Chat

class MessageProcessor:
    def __init__(self, client):
        self.client = client
        self.queue = asyncio.Queue()

    async def get_author(self, sender):
        """Get author name message."""
        if isinstance(sender, User):  # IF USER
            return sender.username or sender.first_name or sender.last_name or ""
        elif isinstance(sender, (Channel, Chat)):  # IF CHANNEL OR CHAT
            return sender.title or ""
        return ""

    async def download_media(self, message):
        """Download media from message."""
        files = []
        if message.media:
            file_name = await self.client.download_media(message.media)
            if file_name:
                files.append(file_name)
        return files

    async def process_reply(self, message):
        """Process reply message."""
        if message.reply_to and message.reply_to.reply_to_top_id:
            original_message = await message.get_reply_message()
            if original_message:
                original_author_name = await self.get_author(original_message.sender)
                return {
                    "author": original_author_name,
                    "content": original_message.message or ""
                }
        return None

    async def process_message(self, message):
        """Combines all the logic for proccessing a single message."""
        # GET AUTHOR
        author_name = await self.get_author(message.sender)
        # MAIN MESSAGE TEXT
        message_content = message.message
        # DOWNLOAD FILES
        files = await self.download_media(message)
        # PROCESSING THE RESPONSE (if any)
        reply_to = await self.process_reply(message)

        full_message = f"`{author_name}`\n{message_content}"
        return {
            "content": full_message,
            "files": files,
            "reply_to": reply_to
        }

    def setup_message_handler(self, callback):
        """Setup message handler."""
        @self.client.on(events.NewMessage(incoming=True))
        async def handler(event):
            pass



