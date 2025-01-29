import asyncio
from config.config_loader import ConfigLoader
from services.telegram_client import TelegramClientService
from services.message_processor import MessageProcessor


async def main():
    config = ConfigLoader()
    api_id = config.get_config("API_ID")
    api_hash = config.get_config("API_HASH")

    # Ініціалізація TelegramClientService
    telegram_service = TelegramClientService(api_id=api_id, api_hash=api_hash)

    # Ініціалізація MessageProcessor
    processor = MessageProcessor(telegram_service.client)

    await telegram_service.connect()

    try:
        # Канал для обробки
        source_channel = config.get_config("SOURCE_CHANNEL")
        await processor.get_message(source_channel)  # Підписка на нові повідомлення

        # Ітерація по отриманих повідомленнях
        async for message_data in processor:
            print(f"Processed message: {message_data}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await telegram_service.disconnect()


if __name__ == "__main__":
    asyncio.run(main())