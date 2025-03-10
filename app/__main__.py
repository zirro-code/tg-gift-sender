import asyncio
import os
from datetime import datetime

from loguru import logger
from pyrogram.client import Client


async def main():
    logger.info(f"Started at {datetime.now().isoformat()}")

    async with Client(
        os.environ["TELEGRAM_ACCOUNT_NAME"],
        os.environ["TELEGRAM_ACCOUNT_HASH_ID"],
        os.environ["TELEGRAM_ACCOUNT_API_HASH"],
    ) as app:
        logger.info("Started updating dialogs")
        # Update list of known contacts for pyrogram to know where to read from
        async for _ in app.get_dialogs():  # type: ignore
            pass
        logger.info("Finished updating dialogs")

        gift_id_to_send: int = int(os.getenv("GIFT_ID_TO_SEND", 5170233102089322756))
        chat_id_to_send_gift: int = int(os.environ["CHAT_ID_TO_SEND_GIFT"])

        for i in range(1, int(os.environ["AMOUNT_OF_GIFTS_TO_SEND"]) + 1):  # type: ignore
            await app.send_gift(
                chat_id=chat_id_to_send_gift,
                gift_id=gift_id_to_send,
                # text=f"Я тебя люблю, и сейчас я напишу это со всех своих аккаунтов. Прогресс: {i}",  # type: ignore # noqa
                text=os.getenv("GIFT_TEXT", ""),
            )


if __name__ == "__main__":
    asyncio.run(main())
