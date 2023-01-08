import asyncio
import telegram
from dotenv import load_dotenv
import os

load_dotenv()

DEV_ID = int(os.getenv("DEV_ID"))


async def main():
    bot = telegram.Bot(os.getenv("TOKEN"))
    async with bot:
        await bot.send_message(DEV_ID, "Loaded")
        print(await bot.get_updates())


if __name__ == "__main__":
    asyncio.run(main())
