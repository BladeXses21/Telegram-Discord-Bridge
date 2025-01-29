
class ChannelForwarder:
    def __init__(self, telegram_service, message_handler):
        self.telegram_service = telegram_service
        self.message_handler = message_handler

    async def forward_messages(self, source_channel, target_channel):
        async for message in self.telegram_service.get_messages(source_channel):
            processed_message = self.message_handler.process_message(message)
            await self.telegram_service.send_message(target_channel, processed_message)