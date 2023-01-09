import asyncio
import telegram
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

sql_engine = create_engine(
    os.getenv("DB")
    + "+"
    + os.getenv("DB_DRIVER")
    + "://"
    + os.getenv("DB_USER")
    + ":"
    + os.getenv("DB_PASSWORD")
    + "@"
    + os.getenv("DB_HOST")
    + ":"
    + os.getenv("DB_PORT")
    + "/"
    + os.getenv("DB_DB"),
    echo=True,
    future=True,
)
sql_engine.connect()
print(sql_engine)

DEV_ID = int(os.getenv("DEV_ID"))


async def main():
    bot = telegram.Bot(os.getenv("TOKEN"))
    async with bot:
        await bot.send_message(DEV_ID, "Loaded\n" + str(sql_engine))
        print(await bot.get_updates())


if __name__ == "__main__":
    asyncio.run(main())
